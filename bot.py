from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os

TOKEN = os.getenv("BOT_TOKEN")  # Бери токен из переменных окружения

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет, я живой и флиртую 😏")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()