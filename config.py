import os
from telethon import TelegramClient

api_id = os.environ.get("api_id", None)
api_hash = os.environ.get("api_hash", None)
bot_token = os.environ.get("bot_token", None)

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
