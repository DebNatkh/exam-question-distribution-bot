#! /usr/bin/env python3

from telegram.ext import Updater, CommandHandler
import requests
import re
import os
from random import choice
import csv

D = dict()
given = set()
admins = set()



def register_admin(update, context):
    chat_id = update.message.chat_id
    admins.add(chat_id)
    with open("admins.txt", "w") as f:
        print(*list(admins), file = f)
    context.bot.send_message(chat_id=chat_id, text="Added you to admins list")



def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Использование: /question 3")


def question(update, context):
    chat_id = update.message.chat_id
    category = update.message.text.split()[-1].lower()
    if (category not in os.listdir('questions')):
        text = "Не смог найти такую категорию вопросов"
    else:
        cat_id = f'{chat_id}-{category}'
        if (cat_id in given and category != 'meme'):
            text = "Уже выдал вам задачу на эту категорию"
        else:
            text = f"Вот вопрос на {category}"
    context.bot.send_message(chat_id=chat_id, text=text)
    if (text.startswith("Вот")):
        filename = f"questions/{category}/" + choice(os.listdir(f'questions/{category}/'))
        print(filename)
        doc = open(filename, 'rb')

        if (category != 'meme'):
            for admin in admins:
                context.bot.send_message(chat_id=admin, text=f'User {update.message.from_user} (category: {category}):')
                context.bot.send_document(chat_id=admin, document=doc)
                doc.seek(0)
        context.bot.send_document(chat_id=chat_id, document=doc)

        given.add(cat_id)
        with open("given.txt", "w") as f:
            print(*list(given), file = f)
            

def main():
    updater = Updater('TELEGRAM_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('question', question))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('register_admin_264841956', register_admin))
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    given = set(list(map(str, open("given.txt", "r").readline().split())))
    admins = set(list(map(int, open("admins.txt", "r").readline().split())))
    with open('db.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            D[row[0].lower()] = (row)
    main()