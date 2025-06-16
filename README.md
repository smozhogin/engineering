# Запуск проекта из Docker контейнера
1. Скачиваем из репозитория DockerHub образ Docker
        docker pull smozhogin/engineering_image:1.0.X
2. Создаем Docker контейнер
        docker run -it -e LC_ALL=ru_RU.UTF-8 --gpus all --name engineering --hostname engineering -p 8080:8080 engineering_image:1.0.X
