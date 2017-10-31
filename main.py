# coding: utf-8
from poll import *
from telegram.ext import CommandHandler, Updater
import logging

def help_message():
    return '''Weee, io sono un  POLLetto e ti aiuto a fare roba strana quale creare POLL, (ovvero sondaggi).
Questo è un messaggio di help che hai invocato utilizzando il comando /help. Mo tu tiani.'''

def start(bot, update):
    """Handles the /start command by sending a simple message to the user."""
    bot.send_message(chat_id=update.message.chat_id, text="Ueeee, sono un POLLetto!")

def help(bot, update):
    """Handles the /help command by showing all of the commands."""
    bot.send_message(chat_id=update.message.chat_id, text=help_message())

def start_bot():
    # logging utility
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # the update
    updater = Updater(token='270200425:AAFJpImg5vlnG7xoWmBelIYhpVYm_sQ77-Y')
    disp = updater.dispatcher

    # commands handlers
    disp.add_handler(CommandHandler('start', start))
    disp.add_handler(CommandHandler('help', help))
    disp.add_handler(CommandHandler('poll', poll_handler))

    # start the bot polling
    updater.start_polling()
    
    # idle for using Ctrl-C
    updater.idle()

if __name__ == '__main__':
    start_bot()