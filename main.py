from Plugins.starter import start
from Plugins.manga import Manga
from config import bot

try:
    start()
    Manga()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
