from telethon import events
import Helper.formating_results as format
from API.nhentaiapi import nhentaiapi as nh
from config import bot

class Nhentai():

    @bot.on(events.NewMessage(pattern="/nh"))
    async def event_handler_anime(event):
        if '/nh' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Command must be used like this\n/nh <hentai code\nexample: /nh 339989',
                file='https://tenor.com/view/fujiwara-chika-chika-kaguya-fujiwara-cute-gif-13308132'
            )
        elif '/nh' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = nh.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id,
                "Open this in google chrome",
                file= f"{code}.html"
            )
