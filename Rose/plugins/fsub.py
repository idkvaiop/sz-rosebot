
    
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

CHANNEL_ID = Config.F_SUB_CHANNEL


async def ForceSub(bot: Client, event: Message):
    try:
        await bot.get_chat_member(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID), user_id=event.from_user.id)
    except UserNotParticipant:
        try:
           gh = await bot.send_message(chat_id=event.chat.id,text=f"""
<b>Hello </b>{event.from_user.mention} !,
<b>Due to high overflow on our database (can handle only 10 request), you need to join the channel in order to use me !.</b>
<i>Don't forget to give</i><code>/start</code><i>command again.</i>""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join The Channel", url="https://t.me/TheAkiraBots")]]),disable_web_page_preview=True)
           await asyncio.sleep(10)
           await gh.delete()
           return 400
        except FloodWait as e:
           await asyncio.sleep(e.x)
           fix_ = await ForceSub(bot, event)
           return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Support Group: https://t.me/supunma")
        return 200  
