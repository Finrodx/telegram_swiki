
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wiki_search import wiki_search
import json
import logging

updater = Updater('TOKEN')

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")




def echo(bot, update):




    user_input = update.message.text



    if user_input.split(" ", 1)[0].lower() == "wiki":

        bot.send_message(chat_id=update.message.chat_id, text=wiki_search(user_input.split(" ", 1)[1]))

    else:
        bot.send_message(chat_id=update.message.chat_id, text="error ")








start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)



updater.start_polling()
updater.idle()
