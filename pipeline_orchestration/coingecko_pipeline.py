#!/usr/bin/env python3
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator  # Typically correct location for BashOperator
from datetime import datetime, timedelta
import requests
import json
import subprocess
import time

default_args = {
    'owner': 'etudiant',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fetch_coingecko_data(**kwargs):
    """Récupère les données depuis l'API CoinGecko."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': '100',
        'page': '1',
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        kwargs['ti'].xcom_push(key='raw_data', value=data)
    else:
        raise ValueError(f"Erreur API : {response.status_code}, {response.text}")

def store_raw_data_in_hdfs(**kwargs):
    """Stocke les données brutes dans HDFS avec partition par date."""
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='fetch_data', key='raw_data')
    
    if not data:
        raise ValueError("Aucune donnée reçue depuis fetch_coingecko_data")
    json_data = json.dumps(data)
    local_file = '../../../tmp/coingecko_raw.json'
    
    # subprocess.run(
    #         ["touch","../../../tmp/coingecko_raw.json"],
    #         check=True
    #     )
    with open("../../../tmp/coingecko_raw.json", 'w') as f:
         f.write(json_data)
   
    print("file created ")
    execution_date = kwargs['ds']
    year, month, day = execution_date.split('-')
    hdfs_dir = f"/user/etudiant/crypto/raw/YYYY={year}/MM={month}/DD={day}"
    hdfs_file_path = f"{hdfs_dir}/coingecko_raw.json"
    tranformed_hdfs_dir=f"/user/etudiant/crypto/processed/YYYY={year}/MM={month}/DD={day}"

    try:
        subprocess.run(
            ["docker","exec", "-u", "root" , "namenode", "hdfs", "dfs", "-mkdir", "-p", hdfs_dir],
            check=True
        )
        time.sleep(0.7)
        # subprocess.run(
        #     ["docker","exec", "-u", "root" , "namenode", "hdfs", "dfs", "-mkdir", "-p",tranformed_hdfs_dir],
        #     check=True
        # )
         
        
        print("dir created")
        # subprocess.run(["docker cp /tmp/coingecko_raw.json namenode:/tmp/coingecko_raw.json"],shell=True,check=True)
      
        subprocess.run(
            [f"docker  exec -u root namenode hdfs dfs -put -f ../tmp/coingecko_raw.json {hdfs_dir}"],
            check=True,
            shell=True,
        )
        # print(f"feedback : {a.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande Docker/HDFS: {e}")
        raise

with DAG(
    dag_id='coingecko_ingestion_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    fetch_data = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_coingecko_data
    )
    store_raw_data = PythonOperator(
    task_id='store_raw_data_in_hdfs',
    python_callable=store_raw_data_in_hdfs
)

    mapreduce_job = BashOperator(
    task_id='run_mapreduce_job',
    bash_command="""
          docker exec -i namenode bash -c "
        hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar    -files /tmp/mapper.py,/tmp/reducer.py    -input /user/etudiant/crypto/raw/YYYY=2025/MM=02/DD=27/coingecko_raw.json    -output /user/etudiant/crypto/processed/YYYY=2025/MM=02/DD=27    -mapper mapper.py    -reducer reducer.py"   """
)

    fetch_data >> store_raw_data >> mapreduce_job
