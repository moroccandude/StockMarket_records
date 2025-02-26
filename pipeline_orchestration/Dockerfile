FROM apache/airflow:2.7.0

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


# Copie le fichier du pipeline Coingecko
COPY coingecko_pipeline.py /opt/airflow/dags/coingecko_pipeline.py 
# Reviens à l'utilisateur airflow
USER airflow