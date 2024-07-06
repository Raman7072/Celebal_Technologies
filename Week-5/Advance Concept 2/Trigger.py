# Install Airflow: 
pip install apache-airflow

# Create DAG(Directed Acyclic Graph)
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
def export_to_csv():
    # Your CSV export code here
  
def export_to_parquet():
    # Your Parquet export code here
  
def export_to_avro():
    # Your Avro export code here
  
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}
dag = DAG(
    'data_export',
    default_args=default_args,
    description='Export data to CSV, Parquet, and Avro',
    schedule_interval='@daily',
)
t1 = PythonOperator(
    task_id='export_to_csv',
    python_callable=export_to_csv,
    dag=dag,
)
t2 = PythonOperator(
    task_id='export_to_parquet',
    python_callable=export_to_parquet,
    dag=dag,
)
t3 = PythonOperator(
    task_id='export_to_avro',
    python_callable=export_to_avro,
    dag=dag,
)
t1 >> t2 >> t3
