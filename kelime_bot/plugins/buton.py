from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("๐  ๐ก๐พ๐๐ ๐ฆ๐๐๐ป๐บ ๐ค๐๐๐พ  ๐", url=f"http://t.me/Shark_Game_Bot?startgroup=new")
    ],
    [
        InlineKeyboardButton("๐น๐ท  ๐ฎ๐๐๐พ๐ ", url="t.me/ByWolk"),
        InlineKeyboardButton("โ๏ธ  ๐ข๐๐๐๐บ๐๐ฝ๐ ", url="t.me/StarBotKanal"),
    ]
])



START = """
โข **Merhaba** ๐\n\nโข **Ben Bir Oyun Botuyum** ๐ฎ \n\nโข **รeลitli oyunlar oynamak ve eฤlenceli vakit geรงirmek iรงin benimle oynayabilirsin** โ๐ป \n\nโข **Benimle oynamak iรงin beni bir gruba ekleyip yรถnetici yapman lazim** . ๐ญ
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
