### Запуск проекта из Docker контейнера
1. Скачиваем из репозитория DockerHub образ Docker

        docker pull smozhogin/engineering_image:1.0.X
2. Создаем Docker контейнер и заходим в интерактивном режиме

        docker run -it -e LC_ALL=ru_RU.UTF-8 --gpus all --name engineering --hostname engineering -p 8080:8080 engineering_image:1.0.X
3. Активируем виртуальную среду

        source /app/venv/medic/bin/activate
4. Запускаем Apache Airflow

        airflow standalone
5. В браузере на хостовой машине переходим по URL

        http://localhost:8080/dags/Medic_Pipeline
6. Запускаем DAG-файл на исполнение
