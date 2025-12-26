"""
*************************************************************
Author = @HiIsai -- https://github.com/HiIsai
Date = 26/12/2025
Description = Extracción de Data de Múltiples Ligas de Futbol
*************************************************************
"""

import pandas as pd
from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from utils import data_processing


# -------------------- DEFAULT ARGS --------------------
default_arguments = {
    'owner': 'IsaiPerez',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# -------------------- PYTHON TASK --------------------
def extract_info(**context):
    df = pd.read_csv('/usr/local/airflow/df_ligas.csv')
    df_team = pd.read_csv('/usr/local/airflow/team_table.csv')

    df_data = data_processing(df)

    df_final = pd.merge(df_data, df_team, how='inner', on='EQUIPO')
    df_final = df_final[
        ['ID_TEAM', 'EQUIPO', 'J', 'G', 'E', 'P', 'GF', 'GC',
         'DIF', 'PTS', 'LIGA', 'CREATED_AT']
    ]

    df_final.to_csv('/usr/local/airflow/premier_positions.csv', index=False)


# -------------------- DAG --------------------
with DAG(
    dag_id='FOOTBAL_LEAGUES',
    description='Extracting Data Football Leagues',
    default_args=default_arguments,
    start_date=datetime(2025, 12, 25),
    schedule=None,
    catchup=False,
    tags=['tabla_espn'],
) as dag:

    params_info = Variable.get("feature_info", deserialize_json=True)

    extract_data = PythonOperator(
        task_id='EXTRACT_FOOTBALL_DATA',
        python_callable=extract_info,
    )

    upload_stage = SQLExecuteQueryOperator(
        task_id='upload_data_stage',
        conn_id='demo_conn',
        sql='queries/upload_stage.sql',
        params=params_info,
    )

    ingest_table = SQLExecuteQueryOperator(
        task_id='ingest_table',
        conn_id='demo_conn',
        sql='queries/upload_table.sql',
        params=params_info,
    )

    extract_data >> upload_stage >> ingest_table
