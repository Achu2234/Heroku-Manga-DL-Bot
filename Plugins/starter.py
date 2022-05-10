from telethon import events

from config import bot
from Helper.helper import help_text, start_text


class start:
    @bot.on(events.NewMessage(pattern="/start"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file="https://telegra.ph/file/92cf02b20ff395bd5e9e0.jpg",
        )

    @bot.on(events.NewMessage(pattern="/help"))
    async def event_handler_help(event):
        await bot.send_message(event.chat_id, help_text)

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            "[Channel](https://t.me/AsmSafone)\nThis bot was hosted on Heroku",
        )
