import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2001, 1, 1), schedule="@daily")
def generate_dag2():
    EmptyOperator(task_id="another-daily-task")


generate_dag2()
