from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern="/start"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://tenor.com/view/miko-iino-whisper-to-chika-fujiwara-chika-iino-chika-fujiwara-miko-iino-gif-21696984'
        )

    @bot.on(events.NewMessage(pattern="/help"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Channel](https://t.me/Animemusicarchive6)\nThis bot was hosted on Heroku'
        )
    
