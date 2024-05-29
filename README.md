Для запуска проекта необходимо выполнить следующие команды в терминале:

1) docker run --name postgres_testing_job -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres;
2) pip install poetry(в случае если у вас не установлен);
3) poetry install;
4) manage.py migrate;
5) manage.py runserver;

Для запуска тестов в терминале ввести команду:
1) pytest;

