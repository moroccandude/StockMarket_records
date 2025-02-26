from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import subprocess

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
    
    result = subprocess.run("cd ../../../tmp && pwd", shell=True, capture_output=True, check=True, text=True)
    json_data = json.dumps(data)
    local_file = './coingecko_raw.json'

   

    print(result.stdout)
    subprocess.run(
            ["touch","./coingecko_raw.json"],
            check=True
        )
    with open(local_file, 'w') as f:
         f.write(json_data)

    execution_date = kwargs['ds']
    year, month, day = execution_date.split('-')
    hdfs_dir = f"/user/etudiant/crypto/raw/YYYY={year}/MM={month}/DD={day}"
    hdfs_file_path = f"{hdfs_dir}/coingecko_raw.json"

    try:
        subprocess.run(
            ["docker","exec", "-u", "root" , "namenode", "hdfs", "dfs", "-mkdir", "-p", hdfs_dir],
            check=True
        )
        subprocess.run(["docker cp /tmp/coingecko_raw.json namenode:/tmp/coingecko_raw.json"],shell=True,check=True)
        subprocess.run(
            ["pwd","&&","docker","exec","-u", "root", "namenode", "hdfs", "dfs", "-put", "-f","/tmp/coingecko_raw.json",hdfs_dir],
            check=True,
            shell=True
        )
        print(f"Données stockées dans HDFS : {hdfs_file_path}")
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

    fetch_data >> store_raw_data
