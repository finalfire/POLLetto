# coding: utf-8
from telegram.ext import CommandHandler, Updater
import logging

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ueeee, sono un POLLetto!")

def start_bot():
    # logging utility
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # the update
    updater = Updater(token='270200425:AAFJpImg5vlnG7xoWmBelIYhpVYm_sQ77-Y')
    disp = updater.dispatcher

    # commands handlers
    start_handler = CommandHandler('start', start)
    disp.add_handler(start_handler)

    # start the bot polling
    updater.start_polling()

if __name__ == '__main__':
    start_bot()
