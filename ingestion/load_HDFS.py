from datetime import datetime, timedelta
import json
import subprocess

def store_raw_data_in_hdfs(**context):
    """Stocke les données brutes dans HDFS avec partition par date."""
    data = context['ti'].xcom_pull(key='raw_data')
    json_data = json.dumps(data)

    # Temporary local file path
    local_file = './tmp/coingecko_raw.json'
    with open(local_file, 'w') as f:
        f.write(json_data)

    # Construct HDFS path based on execution date
    execution_date = context['ds']
    year, month, day = execution_date.split('-')
    hdfs_dir = f"/user/etudiant/crypto/raw/YYYY={year}/MM={month}/DD={day}"
    hdfs_file_path = f"{hdfs_dir}/coingecko_raw.json"
    print(hdfs_dir)
    # Create HDFS directory inside the Docker container
    subprocess.run(["docker", "exec", "namenode", "hdfs", "dfs", "-mkdir", "-p", hdfs_dir])

    # Put the raw data into HDFS inside the Docker container
    subprocess.run(["docker", "exec", "namenode", "hdfs", "dfs", "-put", "-f", local_file, hdfs_file_path])

    # Optional: Add a success log or return statement
    print(f"Data successfully stored in HDFS at {hdfs_file_path}")

    # Optional: Clean up local file after uploading to HDFS
    # subprocess.run(["rm", local_file])















# ------------------
# def store_raw_data_in_hdfs(**context):
#     """Stocke les données brutes dans HDFS avec partition par date."""
#     data = context['ti'].xcom_pull(key='raw_data')
#     json_data = json.dumps(data)

#     # Chemin local temporaire
#     local_file = '/tmp/coingecko_raw.json'
#     with open(local_file, 'w') as f:
#         f.write(json_data)

#     # On construit le chemin HDFS à partir de la date d'exécution
#     execution_date = context['ds']  # ex: '2025-01-01'
#     year, month, day = execution_date.split('-')
#     hdfs_dir = f"/user/etudiant/crypto/raw/YYYY={year}/MM={month}/DD={day}"
#     hdfs_file_path = f"{hdfs_dir}/coingecko_raw.json"

#     # Création du répertoire et mise en HDFS
#     subprocess.run(["hdfs", "dfs", "-mkdir", "-p", hdfs_dir])
#     subprocess.run(["hdfs", "dfs", "-put", "-f", local_file, hdfs_file_path])
