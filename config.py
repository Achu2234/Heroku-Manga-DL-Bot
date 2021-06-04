import os
from telethon import TelegramClient

api_hash = os.environ.get('API_HASH')
api_id = os.environ.get('API_ID')
bot_token = os.environ.get('BOT_TOKEN')

bot = TelegramClient('bot', api_hash, api_id).start(bot_token=bot_token)
