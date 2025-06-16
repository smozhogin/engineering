# Конвейер Apache Airflow в задаче машинного обучения
## Архитектура проекта
### Расположение проекта в среде Linux Ubuntu 24.04

    app/
    ├── project/
    │   └── medic_pipeline/
    └── venv/
        └── medic/

## Запуск проекта из Docker-контейнера
1. Скачиваем из репозитория DockerHub образ Docker

        docker login
        docker pull smozhogin/engineering_image:1.0.X
3. Создаем Docker контейнер и заходим в интерактивном режиме

        docker run -it -e LC_ALL=ru_RU.UTF-8 --gpus all --name engineering --hostname engineering -p 8080:8080 engineering_image:1.0.X
4. Активируем виртуальную среду

        source /app/venv/medic/bin/activate
5. Запускаем Apache Airflow

        airflow standalone
6. В браузере на хостовой машине переходим по URL ***(Логин: admin, пароль: 123)***

        http://localhost:8080/dags/Medic_Pipeline
7. Запускаем DAG-файл на исполнение
