import os
from dotenv import load_dotenv
from telegram import Bot
import requests


load_dotenv('.env')

BOT_TOKEN = os.getenv('bot_token')
BOT_CHATID = os.getenv('bot_chatID')

# bot = Bot(token= BOT_TOKEN)

def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

