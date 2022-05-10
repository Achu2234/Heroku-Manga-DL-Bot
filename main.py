from Plugins.starter import start
from Plugins.manga import Manga
from Plugins.nhentai import Nhentai
from config import bot

try:
    start()
    Manga()
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
