import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

bot = TelegramClient('bot', 5581574,3a521d96e37a33434633d947f6ed9ee8).start(bot_token=1892981260:AAG4wCUQp-SES4YleNeT4lQoXCid0k4Fajg)
