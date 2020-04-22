from airflow import DAG
from datetime import datetime, timedelta


default_args = {
    "owner": "l.rozhkova",
    "depends_on_past": False,
    "start_date": datetime(2020, 2, 16),
    "email": ["l.rozhkova@s7.ru"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

with DAG('twitter_dag_v1', schedule_interval="@daily",catchup=False) as dag:
    None
