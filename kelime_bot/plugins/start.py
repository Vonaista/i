from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *

@Client.on_message(filters.command("game") & ~filters.private & ~filters.channel & ~filters.edited)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("ā¢ š¹šŗšš¾š šš šŗšš½šŗ š½š¾ššŗš š¾š½š¾š š»šš šššš ššŗš āš» \nā¢ š®šššš š½ššš½ššššŗš šš¼šš /stop šššššššš šššššŗššš ā")
    else:
        await m.reply(f"**{m.from_user.mention}** š³šŗššŗšæššš½šŗš ! \nšŖš¾šššš¾ š®šššš š”šŗšššŗšššš½š .\n\nš„³ šŖš¾šššæšš š®šššššŗš !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
šÆ š±šŗššš½ : {oyun[m.chat.id]['round']}/60 
š šŖš¾šššš¾ :   <code>{kelime_list}</code>
š° šŖšŗššŗšš½šššŗš¼šŗš šÆššŗš : 1
š Ä°ššš¼š : 1. {oyun[m.chat.id]["kelime"][0]}
āš» š“šššššš : {int(len(kelime_list)/2)} 

āļø šŖšŗššššš š§šŗššæšš¾šš½š¾š š£šššš šŖš¾šššš¾šš š”šššš š„³ š„³ š„³
        """
        await c.send_message(m.chat.id, text)
        
