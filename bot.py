import os
import logging

from random import choice

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

from google_album import get_pics_urls_list

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    level=logging.INFO,
    filename=str(__file__).rstrip('.py') + '.log',
    filemode='w',
    format=(
        '%(asctime)s - [%(levelname)s] - in module %(name)s, '
        '%(message)s in line %(lineno)d'
    ),
    encoding='utf-8'
)

logger = logging.getLogger(__name__)

reply_buttons = ReplyKeyboardMarkup(
            keyboard=[['/send_photo']],
            resize_keyboard=True,
            is_persistent=True
        )


async def send_photo(update, context):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=choice(get_pics_urls_list()),
        reply_markup=reply_buttons
    )


async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, two-legged. You're here for some fat cats, aren't you?",
        reply_markup=reply_buttons
    )


if __name__ == '__main__':
    photos = get_pics_urls_list()
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    start_handler = CommandHandler('start', start)
    my_cat_handler = CommandHandler('send_photo', send_photo)
    application.add_handler(start_handler)
    application.add_handler(my_cat_handler)
    application.run_polling()
