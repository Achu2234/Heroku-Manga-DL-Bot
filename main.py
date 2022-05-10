from config import bot
from Plugins.manga import Manga
from Plugins.nhentai import Nhentai
from Plugins.starter import start

try:
    start()
    Manga()
    Nhentai()

except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
