#! /usr/bin/env python3

import os
from random import choice
import filetype
from telegram.ext import Updater, CommandHandler
from tinydb import TinyDB, where

db = TinyDB('db.json')
admins_table = db.table("admins")
given_questions = db.table("given")

quiet_categories = ['meme']


def register_admin(update, context):
    chat_id = update.message.chat_id
    admins_table.insert({'chat_id': chat_id})
    context.bot.send_message(chat_id=chat_id, text="Added you to admins list")


def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Использование: /question 3")


def question(update, context):
    chat_id = update.message.chat_id
    category = update.message.text.split()[-1].lower()
    question_requested: bool = False
    if category not in os.listdir('questions'):
        text = "Не смог найти такую категорию вопросов"
    else:
        if given_questions.search((where('chat_id') == chat_id) & (where('category') == category)):
            text = "Уже выдал вам задачу на эту категорию"
        else:
            text = f"Вот вопрос на {category}"
            question_requested = True
    context.bot.send_message(chat_id=chat_id, text=text)
    if not question_requested:
        return

    filename = f"questions/{category}/" + choice(os.listdir(f'questions/{category}/'))
    print(filename)

    with open(filename, 'rb') as doc:
        if category not in quiet_categories:
            for admin in admins_table.all():
                context.bot.send_message(chat_id=admin['chat_id'],
                                         text=f'User {update.message.from_user} (category: {category}):')
                context.bot.send_document(chat_id=admin['chat_id'], document=doc)
                doc.seek(0)
            given_questions.insert({'chat_id': chat_id, 'category': category})
        if filetype.is_image(filename):
            context.bot.send_photo(chat_id=chat_id, photo=doc)
        else:
            context.bot.send_document(chat_id=chat_id, document=doc)


def main():
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_password = os.getenv('TELEGRAM_BOT_ADMIN_PASSWORD')

    updater = Updater(telegram_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('question', question))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler(f'register_admin_{telegram_password}', register_admin))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
