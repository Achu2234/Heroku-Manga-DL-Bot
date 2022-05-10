from nhentaiapi import nhentaiapi as nh
from telethon import events

import Helper.formating_results as format
from config import bot


class Nhentai:
    @bot.on(events.NewMessage(pattern="/nh"))
    async def event_handler_anime(event):
        if "/nh" == event.raw_text:
            await bot.send_message(
                event.chat_id,
                "Hentai Manga not found Command must be used like this\n/nh <hentai code\nexample: /nh 339989",
                file="https://telegra.ph/file/977679ba01df954a40880.mp4",
            )
        elif "/nh" in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = nh.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id, "Open this in google chrome", file=f"{code}.html"
            )
