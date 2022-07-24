import logging

from pytube import YouTube
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

logging.basicConfig(level=logging.DEBUG, filename='logs.txt')

from yandex import sendToScreen
import config


def start_command_callback(update, context):
    update.message.reply_text(config.start_text)


def help_command_callback(update, context):
    update.message.reply_text(config.help_text)


def message_received(update, context):

    print(update.message)

    if update.message.from_user.id != config.telegram_user_id:
        print("External request blocked!")
        update.message.reply_text("Это бот @vladislav_syrov. Пожалуйста, сделайте своего бота.")
        return

    url = extract_url(update.message)
    video_url = get_video_url(url)
    result = sendToScreen(video_url)

    print(result)

    update.message.reply_text(result + " " + video_url)


last_url = ""
def get_video_url(url):
    global last_url

    if url == last_url:  # Second attempt - trying another player
        yt = YouTube(url).streams.first()
        last_url = url
        return yt.url

    last_url = url

    if "https://www.youtube" in url:
        # Удаляем лишние аргументы (все кроме первого)
        url = url.split("&")[0]

    if "https://youtu.be" in url:
        # Подменяем адрес запроса
        url = "https://www.youtube.com/watch?v=" + url.split("/")[-1]

    # Page parsing and getting video_url here
    return url


def extract_url(message):
    return message.text  # TODO: добавить поиск урла в тексте сообщения


updater = Updater(token=config.telegram_bot_token, request_kwargs=config.proxy)

start_handler = CommandHandler("start", start_command_callback)
help_handler = CommandHandler("help", help_command_callback)
message_handler = MessageHandler(Filters.text, message_received)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(message_handler)

print("Start polling...")

updater.start_polling()
