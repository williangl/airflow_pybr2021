# airflow_pybr2021
Código do tutorial de Airflow ministrado por Tarsis Azevedo e Sávio Teles na Python Brasil 2021


iniciar o webserver do airflow
```shell
poetry run airflow webserver -p 8081
```

iniciar o scheduler sem as DAGs de exemplo:
```shell
AIRFLOW__CORE__LOAD_EXAMPLES=False poetry run airflow scheduler --subdir dags
```

build docker image
```shell
docker build . -t pybr_tutorial
```
