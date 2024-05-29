Для запуска проекта необходимо выполнить следующие команды в терминале:
docker run --name postgres_testing_job -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres;
pip install poetry(в случае если у вас не установлен);
poetry install;
manage.py migrate;
manage.py runserver;

Для запуска тестов в терминале ввести команду:
pytest
