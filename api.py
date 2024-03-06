from datetime import datetime
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='api_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 3, 1),
    catchup=False
) as dag:

  check_api_active_task=HttpSensor(
      task_id='check_api',
      http_conn_id='api_posts',
      endpoint='posts/'

  )




#### with statement
# f = open("example.txt", "w")

# try:
#     f.write("hello world")
# finally:
#     f.close()

# with open("example.txt", "w") as file:
#     file.write("Hello World!")

    