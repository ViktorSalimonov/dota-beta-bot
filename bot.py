import logging
import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ("/random_meme – хочу мем\n"
            "/ww – узнать виверна это кор или саппорт")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def random_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    soup = BeautifulSoup(urlopen('https://dota2.ru/memes/random/'), 'html.parser')
    tag = soup.find_all('div', {'class': 'mems-page__mem bg-main-block'})[0]
    img_url = f"https://dota2.ru/{tag.contents[1].contents[1].attrs['src']}"
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img_url)


async def ww(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Виверна – кор")


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ['TG_TOKEN']).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('random_meme', random_meme))
    application.add_handler(CommandHandler('ww', ww))

    application.run_polling()
