# Конвейер Apache Airflow в задаче машинного обучения

## Архитектура проекта

### Расположение проекта в среде Linux Ubuntu 24.04

    app/
    ├── project/
    │   └── medic_pipeline/
    │       ├── dags/
    │       │   └── pipeline_dag.py
    │       ├── data/
    │       │   └── logistic_regression_model.pkl
    │       ├── etl/
    │       │   ├── data_loader.py
    │       │   ├── data_preprocessor.py
    │       │   ├── model_evaluator.py
    │       │   ├── model_trainer.py
    │       │   └── results_keeper.py
    │       ├── logs/
    │       ├── README.md
    │       └── results/
    └── venv/
        └── medic/
            └── bin/
                ├── activate
                ├── pip
                └── python

### Шаги конвейера

    Загрузка данных --> Предобработка данных --> Обучение модели --> Оценка модели --> Сохранение результатов

1. Загрузка данных
2. Предобработка данных
3. Обучение модели
4. Оценка модели
5. Сохранение результатов  
   В Яндекс.Cloud было создано приложение **medic_pipeline**. По ClientID приложения запрашивается OAuth-токен. Данный токен прописывается в файле config.ini и используется в скрипте при сохранеии файлов на удаленном диске.
   Результаты работы конвейера сохраняются на Яндекс.Диск по пути: https://disk.yandex.ru/d/ofnaZFAvsAnuIQ (общий доступ открыт):

   - Обученная модель логистической регрессии в файле .pkl;
   - Метрики в формате JSON.

### Обработка ошибок

### Логирование

## Запуск проекта из Docker-контейнера
1. Скачиваем из репозитория DockerHub образ Docker

        docker login
        docker pull smozhogin/engineering_image:1.0.X
3. Создаем Docker-контейнер и запускаем в интерактивном режиме

        docker run -it -e LC_ALL=ru_RU.UTF-8 --gpus all --name engineering --hostname engineering -p 8080:8080 engineering_image:1.0.X
4. Активируем виртуальную среду

        source /app/venv/medic/bin/activate
5. Запускаем Apache Airflow

        airflow standalone
6. В браузере на хостовой машине переходим по URL  
   **Логин: admin, пароль: 123**

        http://localhost:8080/dags/Medic_Pipeline
8. Запускаем DAG на исполнение
