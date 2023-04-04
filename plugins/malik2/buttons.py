from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.malik.mbin import malikk
from os import environ




NOTFOUN = InlineKeyboardMarkup([[InlineKeyboardButton("Request", url="https://t.me/Filmyfunda_help_bot")]]) 

GSLB = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/filmyfunda_movies")],[ InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/filmyfunda_movies")]]) 

HSTN = InlineKeyboardMarkup([[InlineKeyboardButton("❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️", url=f"http://t.me/{malikk.u_name}?startgroup=true") ],[ InlineKeyboardButton('♻️ ʜᴇʟᴘ ♻️', callback_data='help'), InlineKeyboardButton('⚡️ᴜᴘᴅᴀᴛᴇs⚡️', url='https://t.me/filmyfunda_movies')],[InlineKeyboardButton('sᴇᴀʀᴄʜ ɪɴʟɪɴᴇ', switch_inline_query_current_chat=''), InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')]])  

HSTNN = InlineKeyboardMarkup([[InlineKeyboardButton('❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️', url=f'http://t.me/{malikk.u_name}?startgroup=true') ],[ InlineKeyboardButton('♻️ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/filmyfunda_movies')],[ InlineKeyboardButton('🔹 ʜᴇʟᴘ 🔹', url=f"http://t.me/{malikk.u_name}?startgroup=help")]])

GROUP_RULES = InlineKeyboardMarkup([[InlineKeyboardButton('♻️ GROUP RULES ♻️', callback_data='group_rules')]])

TFRADE = InlineKeyboardMarkup([[InlineKeyboardButton('♻️ Help ♻️', url=f"http://t.me/{malikk.u_name}?startgroup=help"),InlineKeyboardButton('💎 Updates 💎', url='https://t.me/Filmyfunda_help_bot')],[InlineKeyboardButton('🌴 Bots Channel 🌴', url='https://t.me/filmyfunda_movies')]])
