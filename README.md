## exam-question-distribution-bot

Бот для выдачи вопросов сдающим зачёт или экзамен

Есть несколько категорий вопросов (категория — поддиректория в директории questions)

### Запуск бота:

1. Установить необходимые зависимости
    ```bash
    python3 -m pip install -r requirements.txt
    ```

2. Определить переменные окружения `TELEGRAM_BOT_TOKEN` (токен для HTTP API, полученный
   у [@BotFather](http://t.me/BotFather)) и `TELEGRAM_BOT_ADMIN_PASSWORD` (произвольный пароль, например, `qwerty`):
    ```bash
    export TELEGRAM_BOT_TOKEN="1488440437:AAEstEeMyMSYvOUKc7zAaCy-F5GVM12-oF4"
    export TELEGRAM_BOT_ADMIN_PASSWORD="qwerty"
    ```

3. Запустить бота:
    ```bash
    python3 main.py
    ```

4. Вся информация будет храниться в созданном файле `db.json`. Если вы захотите очистить историю бота, можно удалить
   этот файл.

### Использование:

* Чтобы получить вопрос, нужно написать `/question cat`, где `cat` — категория вопроса.

* Чтобы видеть, кто какой вопрос получил, нужно написать `/register_admin_qwerty` (или вместо `qwerty` — любой другой
  установленный вами пароль). После этого все выданные вопросы будут пересылаться вам.

## exam-question-distribution-bot

Bot for issuing questions for an exam

There are several categories of questions (the category is a subdirectory in the `questions` directory)

### Launching the bot:

1. Install the necessary dependencies
    ```bash
    python3 -m pip install -r requirements.txt
    ```

2. Define environment variables `TELEGRAM_BOT_TOKEN` (the HTTP API token obtained
   from [@BotFather](http://t.me/BotFather)) and `TELEGRAM_BOT_ADMIN_PASSWORD` (an arbitrary password, i.e. `qwerty`):
    ```bash
    export TELEGRAM_BOT_TOKEN="1488440437:AAEstEeMyMSYvOUKc7zAaCy-F5GVM12-oF4"
    export TELEGRAM_BOT_ADMIN_PASSWORD="qwerty"
    ```

3. Launch the bot:
    ```bash
    python3 main.py
    ```

4. All information will be stored in the created file `db.json`. If you want to clear the bot's history, you can delete
   this file.

### Usage:

* To obtain a question, write `/question cat`, where `cat` is the category of the question.

* To be able to see who got which question, write `/register_admin_qwerty `(or any other password you set instead
  of `qwerty`). After that, all issued questions will be forwarded to you.