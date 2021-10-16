from datetime import datetime
from random import randint
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.docker_operator import DockerOperator


with DAG(
    "movie_chooser_v1",
    tags=["pybr-tutorial"],
    start_date=datetime(2021, 10, 14),
    catchup=False,
    schedule_interval="*/5 * * * *",
) as dag:
    start = DummyOperator(task_id="start_task")

    # movie_choosen_1 = PythonOperator(
    #     task_id="choose_movie_1", python_callable=choose_movie, dag=dag
    # )
    # movie_choosen_2 = PythonOperator(
    #     task_id="choose_movie_2", python_callable=choose_movie, dag=dag
    # )
    # movie_choosen_3 = PythonOperator(
    #     task_id="choose_movie_3", python_callable=choose_movie, dag=dag
    # )

    tasks = []
    genres = ["Romance", "Comedy", "Fantasy", "Drama", "Animation"]
    for genre in genres:
        task = DockerOperator(
            task_id=f"movie_by_genre_{genre.lower()}",
            dag=dag,
            image="pybr-tutorial",
            auto_remove=True,
            command=["python", "dags/movie_chooser.py", genre]
        )
        tasks.append(task)

    end = DummyOperator(task_id="end_task", dag=dag)

    start >> tasks >> end
