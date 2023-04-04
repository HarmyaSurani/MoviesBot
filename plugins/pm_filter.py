# Kanged From @sahid malik 
import asyncio
import re, random
import datetime
import random
import ast
import math
import string
import contextlib
import time
from plugins.malik2.buttons import HSTN
from plugins.malik.extra import GHHMT, INST, IYGL, GOOGL, SONGS, RULES_ALERT, GROUP_Rules, SMART_PIC, STTS, MQTT, TEL, MQTTP, PPC, REPORT, PPI, SHARETXT, WALL, PURGE, MUTE, SS_ALERT, STKR, WRITE, FONTS, MY_DETALS, MQTTTM
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script, ALURT_FND, ADDG
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from plugins import malik 
from info import RQST_CHANNEL, ADMINS, DEL_SECOND, AUTH_CHANNEL, VIDEO_VD, AUTH_USERS, PICS, M_NT_F, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE, REQ_GRP, TUTORIAL_LINK_1, TUTORIAL_LINK_2, REQ_GRP 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram import Client, filters, enums 
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import replace_words, get_shortlink, get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}



@Client.on_message(filters.group & filters.text & filters.incoming &~ filters.chat(REQ_GRP))
async def give_filter(client, message):
    k = await manual_filters(client, message)
    if k == False:
        await auto_filter(client, message)



@Client.on_message(filters.text & filters.group & filters.incoming & filters.chat(REQ_GRP))
async def req_grp_results(bot, msg: Message):
    if msg.text.startswith("/"): return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", msg.text):
        return
    files = None
    if 2 < len(msg.text) < 100:
        search = msg.text
        files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)

    if not files:

        # request movie from admin
        msg_id = msg.id
        user_id = msg.from_user.id
        user_name = msg.from_user.mention
        user_query = msg.text
        reply = search.replace(" ", '+')
        reply_markup1 = [
            [
                InlineKeyboardButton("🔍 Click here to Check Spilling ✅", url=f"https://www.google.com/search?q={reply}+movie"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Updated  ✅",
                    callback_data=f'rq#up#{msg_id}#{user_query}',
                ),
                InlineKeyboardButton(
                    text="Already uploaded ✅",
                    callback_data=f'rq#au#{msg_id}#{user_query}',
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Not released in OTT yet",
                    callback_data=f'rq#nr#{msg_id}#{user_query}',
                ),            
                InlineKeyboardButton(
                    text="Not Available in hindi",
                    callback_data=f'rq#ntaih#{msg_id}#{user_query}',
                ),    
            ],
            [
                InlineKeyboardButton(
                    text="Not Dubb in hindi",
                    callback_data=f'rq#ntdih#{msg_id}#{user_query}',
                ), 
                InlineKeyboardButton(
                    text="Not Available in kannada",
                    callback_data=f'rq#ntaik#{msg_id}#{user_query}',
                ),                       

            ],
            [
                InlineKeyboardButton(
                    text="Already uploaded ✅",
                    callback_data=f'rq#alupd#{msg_id}#{user_query}',
                ),
                InlineKeyboardButton(
                    text="Go to Google check your spelling",
                    callback_data=f'rq#cysp#{msg_id}#{user_query}',
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Not released yet",
                    callback_data=f'rq#nry#{msg_id}#{user_query}',
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Send imdb Link",
                    callback_data=f'rq#simd#{msg_id}#{user_query}',
                ),
                InlineKeyboardButton(
                    text="Not available",
                    callback_data=f'rq#na#{msg_id}#{user_query}',
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close_data"          
                ),
            ],
        ]
        await bot.send_message(RQST_CHANNEL, text=f"#MovieRequest\n\nGroup 1 👉 <a href=https://t.me/+gMx2ry12kODI1>Click Here</a>\n\nGroup 2 👉 <a href=https://t.me/+ulaVbqKvS3NjU9>Click Here</a>\n\nUser <b>{user_name}</b>\n\nrequested for <code>{user_query}</code>\n\nReply to <code>/pm {user_id} {msg_id} message</code>`\n\nView message 👉 <a href=https://t.me/+jk7skw3kIU45MGE1/{msg_id}>Click Here</a>\n😎", reply_markup=InlineKeyboardMarkup(reply_markup1))

        user_info = temp.USER_SPELL_CHECK.get(msg.from_user.id)
        if not user_info or time.time() - user_info >= 60:
            temp.USER_SPELL_CHECK[msg.from_user.id] = time.time()
            reply = search.replace(" ", '+')
            reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton("ɪɴsᴛʀᴜᴄᴛɪᴏɴs", callback_data='inst'),
            InlineKeyboardButton("ᴅᴏɴᴀᴛɪᴏɴ", url="https://t.me/donation_for_service/3")
            ],[
            InlineKeyboardButton("🔍 ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ sᴘɪʟʟɪɴɢ ✅", url=f"https://www.google.com/search?q={reply}+movie")
            ]]  
            )
            a = await msg.reply_photo(
                photo=(MQTTP),
                caption=(MQTTTM.format(msg.from_user.mention, search)),
                reply_markup=reply_markup                 
            )
            await asyncio.sleep(30)
            await a.delete()
        return

    await msg.reply(f'<b>Dear.</b> {msg.from_user.mention}  \n\n👉 <code>{total_results}</code> 👈 <b>results are already available for your request</b> 👉 <code>{search}</code> 👈 <b>in our bot..\n\n plz Go back our group and type movie name</b> 👇',  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔹 Movies request group🔹",url="https://t.me/+Zcwr0lahhRA3NTNl"),]]),parse_mode=enums.ParseMode.HTML),



@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(f"⚠️ 𝗛𝗲𝘆, {query.from_user.first_name}.. \n\n𝗦𝗲𝗮𝗿𝗰𝗵 𝗬𝗼𝘂𝗿 𝗢𝘄𝗻𝗲𝗿 𝗙𝗶𝗹𝗲,\n\n⚠️𝗗𝗼𝗻'𝘁 𝗖𝗹𝗶𝗰𝗸 𝗢𝘁𝗵𝗲𝗿𝘀 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 😬", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.", show_alert=True)
        return

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    settings = await get_settings(query.message.chat.id)
    if settings['button']:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'files#{file.file_id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if 0 < offset <= temp.multi_buttons:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - temp.multi_buttons
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton(text="ᴘᴀɢᴇꜱ", callback_data="pages"),
             InlineKeyboardButton("⫷ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"ᴘᴀɢᴇꜱ {math.ceil(int(offset) / temp.multi_buttons) + 1} / {math.ceil(total / temp.multi_buttons)}",
                                  callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(text="ᴘᴀɢᴇꜱ ", callback_data="pages"),
             InlineKeyboardButton(f" {math.ceil(int(offset) / temp.multi_buttons) + 1} / {math.ceil(total / temp.multi_buttons)}", callback_data="pages"),
             InlineKeyboardButton("ɴᴇxᴛ ⫸", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("⫷ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f" {math.ceil(int(offset) / temp.multi_buttons) + 1} / {math.ceil(total / temp.multi_buttons)}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⫸", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    btn.insert(0, 
        [
            InlineKeyboardButton('ʙᴏᴛ ɪɴғᴏ', callback_data='ss_alert'),
            InlineKeyboardButton('ʀᴜʟᴇs', callback_data='rules_alert')
        ],
    )
    btn.insert(1, [
        InlineKeyboardButton("HOW TODOWNLOAD", url=malik.int_link)
    ])
    try:
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()


@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(f"⚠️ 𝗛𝗲𝘆, {query.from_user.first_name}.. \n\n𝗦𝗲𝗮𝗿𝗰𝗵 𝗬𝗼𝘂𝗿 𝗢𝘄𝗻𝗲𝗿 𝗙𝗶𝗹𝗲,\n\n⚠️𝗗𝗼𝗻'𝘁 𝗖𝗹𝗶𝗰𝗸 𝗢𝘁𝗵𝗲𝗿𝘀 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 😬", show_alert=True)
    if movie_  == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.id)
    if not movies:
        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Checking for Movie in database...')
    k = await manual_filters(bot, query.message, text=movie)
    if k == False:
        files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
        if files:
            k = (movie, files, offset, total_results)
            await auto_filter(bot, query, k)
        else:
           kbb = await query.message.edit(text=(malik.mntf), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('💢 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 💢', url=malik.notfoun),]]),parse_mode=enums.ParseMode.HTML)                                                                                                                                            
           await asyncio.sleep(12)
           await kbb.delete()

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == enums.ChatType.PRIVATE:
            grpid = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return await query.answer('Piracy Is Crime')
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return await query.answer('Piracy Is Crime')

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return await query.answer('Piracy Is Crime')

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!", show_alert=True)
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("That's not for you!!", show_alert=True)
    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        act = query.data.split(":")[2]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}"),
             InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return await query.answer('Piracy Is Crime')
    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title

        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occurred!!', parse_mode="md")
        return await query.answer('Piracy Is Crime')
    elif "disconnect" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text(
                f"Some error occurred!!",
                parse_mode="md"
            )
        return await query.answer('Piracy Is Crime')
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text(
                f"Some error occurred!!",
                parse_mode="md"
            )
        return await query.answer('Piracy Is Crime')
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return await query.answer('Piracy Is Crime')
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert, show_alert=True)
    if query.data.startswith("file"):

        # User Verifying
        user_id = query.from_user.id
        is_second_shortener = await db.use_second_shortener(user_id)
        if not await db.is_user_verified(user_id) or is_second_shortener:

            verify_id = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=7)
            )

            await db.create_verify_id(user_id, verify_id)

            how_to_download_link = (
                TUTORIAL_LINK_2 if is_second_shortener else TUTORIAL_LINK_1
            )

            buttons = [
                [
                    InlineKeyboardButton(
                        text="🔹 Click hare to Verify 🔹",
                        url=await get_shortlink(
                            f"https://telegram.me/{temp.U_NAME}?start=notcopy_{user_id}_{verify_id}",
                            is_second_shortener,
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🌀 How to verify 🌀", url=how_to_download_link
                    )
                ],
            ]

            text = f"You'r not verified today. Please verify now and get unlimited access for 1 day)"
            if query.message.chat.type == "private":
                return await query.message.reply_text(
                    text, reply_markup=InlineKeyboardMarkup(buttons)
                )

        # User Verifying

        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = files.caption
        settings = await get_settings(query.message.chat.id)
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
            f_caption = f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"

        try:
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
                return
            elif settings['botpm']:
                await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
                return
            else:
                dmm = await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    protect_content=True if ident == "filep" else False 
                )
                await query.answer('Check PM, I have sent files in pm', show_alert=True)
        except UserIsBlocked:
            await query.answer('Unblock the bot mahn !', show_alert=True)
        except PeerIdInvalid:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
        except Exception as e:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
    elif query.data.startswith("checksub"):
        user_id = query.from_user.id
        # User Verifying
        is_second_shortener = await db.use_second_shortener(user_id)
        if not await db.is_user_verified(user_id) or is_second_shortener:
            verify_id = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=7)
            )
            how_to_download_link = (
                TUTORIAL_LINK_2 if is_second_shortener else TUTORIAL_LINK_1
            )
            await db.create_verify_id(user_id, verify_id)

            buttons = [
                [
                    InlineKeyboardButton(
                        text="🔹 Click hare to Verify 🔹",
                        url=await get_shortlink(
                            f"https://telegram.me/{temp.U_NAME}?start=notcopy_{user_id}_{verify_id}",
                            is_second_shortener,
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🌀 How to verify 🌀", url=how_to_download_link
                    )
                ],
            ]
            num = 2 if is_second_shortener else 1
            text = f"You'r not verified today. Please verify - ({num}) now and get unlimited access for 1 day)"
            if query.message.chat.type == "private":
                return await query.message.reply_text(
                    text, reply_markup=InlineKeyboardMarkup(buttons)
                )

        # User Verifying


        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒...\n\n 😳 bro niche diye gye updates channel ko join karo  jab tak aap updates channel join nahi karte tab tak bot apko movie nahi dega! ", show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption = f_caption
        if f_caption is None:
            f_caption = f"{title}"
        await query.answer()
        dm = await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption,
            protect_content=True if ident == 'checksubp' else False
        )
        if settings['auto_deletee']:
            await asyncio.sleep(25)
            await dm.delete()
    elif query.data == "pages":
        await query.answer()
    elif query.data == "start":
        reply_markup = HSTN
        await query.message.edit_text(
            text=(script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.MARKDOWN
        )
        await query.answer('Piracy Is Crime')
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton(' ᴍᴀɴᴜᴇʟ ғɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('ᴀᴜᴛᴏ ғɪʟᴛᴇʀ', callback_data='autofilter'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴs', callback_data='coct')
        ], [
            InlineKeyboardButton('ᴇxᴛʀᴀ ᴍᴏᴅᴇs', callback_data='GHHM'),
            InlineKeyboardButton('ʜᴏᴍᴇ ', callback_data='start'),
            InlineKeyboardButton('sᴏɴɢs', callback_data='songs')
        ], [
            InlineKeyboardButton('sᴛᴀᴛs', callback_data='stats'),
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tel'),
            InlineKeyboardButton('ᴏᴡɴᴇʀ', callback_data='my_detals')
        ], [
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb'),
            InlineKeyboardButton('ᴠɪᴅᴇᴏ', callback_data='video'),
            InlineKeyboardButton('ғɪʟᴇ-sᴛᴏʀᴇ', callback_data='malikk')
        ], [
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='mute'),
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purges'),
        ], [
            InlineKeyboardButton('ғᴏɴᴛs', callback_data='fonts'),
            InlineKeyboardButton('sᴛɪᴄᴋᴇʀ', callback_data='stkr'),
            InlineKeyboardButton('ᴡʀɪᴛᴇ ᴛᴇxᴛ', callback_data='write'),
        ], [
            InlineKeyboardButton('ꜱʜᴀʀᴇ ᴛᴇxᴛ', callback_data='sharetxt'),
            InlineKeyboardButton('ᴡᴀʟʟᴘᴀᴘᴇʀ', callback_data='wall'),
            InlineKeyboardButton('G-ᴛʀᴀɴsʟᴀᴛᴇ', callback_data='googl'),
        ], [
            InlineKeyboardButton('🚶‍♀ 𝐁𝐀𝐂𝐊 🚶‍♀', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('🌴 Main ᴄʜᴀɴɴᴇʟ 🌴', url='https://t.me/filmyfunda_movies'),
            InlineKeyboardButton('♥️ sᴏᴜʀᴄᴇ', callback_data='source')
        ], [
            InlineKeyboardButton('ʜᴏᴍᴇ ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏᴄᴇ', callback_data='close_data')
        ], [
            InlineKeyboardButton('📞 ᴏᴡɴᴇʀ', url='https://t.me/bhatmanju'),
            InlineKeyboardButton('❤️ ᴅᴏɴᴀᴛɪᴏɴ ❤️', callback_data='malik')
        ], [
            InlineKeyboardButton('🚶‍♀ 𝐛𝐚𝐜𝐤 🚶‍♀', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME, temp.USERNAME, temp.NAME), 
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "GHHM":
        buttons = [[
            InlineKeyboardButton('🌴 Main Channel 🌴', url='https://t.me/filmyfunda_movies'),
            InlineKeyboardButton('𝗘𝘅𝘁𝗿𝗮 𝗠𝗼𝗱𝗲𝘀', callback_data='extra'),
            InlineKeyboardButton('𝗘𝘅𝘁𝗿𝗮', callback_data='mbbumm')
        ], [
            InlineKeyboardButton('🚶‍♀ 𝙱𝙰𝙲𝙺 🚶‍♀', callback_data='start'),
            InlineKeyboardButton('🔐 𝗖𝗹𝗼𝘀𝗲 🔐', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GHHN_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "urlshort":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.URLSHORT_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "report":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(REPORT),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "sharetxt":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(SHARETXT),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "wall":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(WALL),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "googl":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(GOOGL),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "mute":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(MUTE),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "purges":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(PURGE),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "fonts":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(FONTS),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "stkr":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(STKR),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "my_detals":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(MY_DETALS.format(query.from_user.mention)),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "write":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(WRITE),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "tel":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(TEL),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "malikk":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FILESTORE_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "group_rules":
        buttons = [[
            InlineKeyboardButton('💢 close 💢', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(GROUP_Rules),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "video":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDEO_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "songs":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=(SONGS),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "owner":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='start'),
            InlineKeyboardButton('❗️ CONTACT ❗️', url='https://t.me/bhatmanju')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.OWNER_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "urlshortn":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.URLSHORTN_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "mbbumm":
        buttons = [[
            InlineKeyboardButton('✳️ Add Me To Your Groups ❇️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GHHM_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "inst":
        await query.answer(INST, show_alert=True)
        return
    elif query.data == "ss_alert":
        await query.answer(SS_ALERT.format(query.from_user.first_name),show_alert=True)
        return
    elif query.data == "rules_alert":
        await query.answer(RULES_ALERT.format(query.from_user.first_name),show_alert=True)
        return
    elif query.data == "videos":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDEOS_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "ytthumb":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.YTTHUMB_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "source":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        z=await query.message.reply_sticker("CAACAgUAAxkBAAIOKmL4bD2FjcsqAAEW5ARMXLzyQbJ4CgACgAMAAuMV0FVUQzIP1OspYh4E")
        await asyncio.sleep(2)
        await z.delete()
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "malik":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MALIK_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "dinette":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.DINETTE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help'),
            InlineKeyboardButton('⏹️ 𝗕𝘂𝘁𝘁𝗼𝗻𝘀 ⏹', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='manuelfilter')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='help'),
            InlineKeyboardButton('👮‍♂️ owner👮', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='extra')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='close_data'),
            InlineKeyboardButton('♻️ Refresh ♻️', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        malik = await query.message.reply('malik')
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.reply_photo(
            photo=(PPC),
            caption=(STTS.format(total, users, chats, monsize, free)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(2)
        await malik.delete()
        return 
    elif query.data == "stats":
        await query.answer("Fetching MongoDb DataBase")
        buttons = [[
            InlineKeyboardButton('🚶 𝗕𝗮𝗰𝗸 🚶', callback_data='close_data'),
            InlineKeyboardButton('♻️ Refresh ♻️', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        malik = await query.message.reply_sticker('malik')
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.reply_photo(
            photo=(PPC),
            caption=(STTS.format(total, users, chats, monsize, free)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(2)
        await malik.delete()
        return 
    elif query.data.startswith("setgs"):
        ident, set_type, status, grp_id = query.data.split("#")
        grpid = await active_connection(str(query.from_user.id))

        if str(grp_id) != str(grpid):
            await query.message.edit("Your Active Connection Has Been Changed. Go To /settings.")
            return await query.answer('Piracy Is Crime')

        if status == "True":
            await save_group_settings(grpid, set_type, False)
        else:
            await save_group_settings(grpid, set_type, True)

        settings = await get_settings(grpid)

        if settings is not None:
            buttons = [
                [
                    InlineKeyboardButton('Filter Buttons',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                    InlineKeyboardButton('Single' if settings["button"] else 'Double',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Bot pm', callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ YES' if settings["botpm"] else '❌ NO',
                                         callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('File Secure',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ YES' if settings["file_secure"] else '❌ NO',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('IMDB', callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ YES' if settings["imdb"] else '❌ NO',
                                         callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Spell Check',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ YES' if settings["spell_check"] else '❌ NO',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Welcome msg', callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ ON' if settings["welcome"] else '❌ OFF',
                                         callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Spell Auto Delete',
                                         callback_data=f'setgs#spell_auto_delete#{settings["spell_auto_delete"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ ON' if settings["spell_auto_delete"] else '❌ OFF',
                                         callback_data=f'setgs#spell_auto_delete#{settings["spell_auto_delete"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Manual filter',
                                         callback_data=f'setgs#manual_filter#{settings["manual_filter"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ ON' if settings["manual_filter"] else '❌ OFF',
                                         callback_data=f'setgs#manual_filter#{settings["manual_filter"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Movies Auto Delete',
                                         callback_data=f'setgs#auto_deletee#{settings["auto_deletee"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ ON' if settings["auto_deletee"] else '❌ OFf',
                                         callback_data=f'setgs#auto_deletee#{settings["auto_deletee"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Auto Filter',
                                         callback_data=f'setgs#auto_filters#{settings["auto_filters"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✔ ON' if settings["auto_filters"] else '❌ OFF',
                                         callback_data=f'setgs#auto_filters#{settings["auto_filters"]}#{str(grp_id)}')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_reply_markup(reply_markup)
    elif query.data.startswith("rq#"):
        _, status, message_id, user_query = query.data.split("#", maxsplit=3)
        dict_info = {"alupd":"Already uploaded ✅", "nry":"Not released yet", "ntaik":"Not available in kannada", "ntaih":"Not available in Hindi", "ntdih":"Not Dubb in Hindi", "cysp":"Go to Google and check your spelling  <b><a href=https://www.google.com>𝐆𝐨𝐨𝐠𝐥𝐞</a></b>", "simd":"Send imdb link", "au":"Already uploaded ✅ \n\n Go to Google and check your spelling  <b><a href=https://www.google.com>𝐆𝐨𝐨𝐠𝐥𝐞</a></b>", "up":"Updated  ✅", "nr":"Not released OTT yet", "na":"Not available"}

        user_message = await client.get_messages(REQ_GRP, int(message_id))
        user_id = user_message.from_user.id
        user_mention = (await client.get_users(user_message.from_user.id)).mention

        text = f"Hey {user_mention}... \n\nYour movie 👉 {dict_info[status]}"
        await client.send_message(REQ_GRP, text, reply_to_message_id=int(message_id))
        bbb = await query.edit_message_text("Request has been updated")
        await asyncio.sleep(20)
        await bbb.delete()       

    await query.answer('Piracy Is Crime')



async def auto_filter(client, msg, spoll=False):
    if not spoll:
        message = msg
        settings = await get_settings(message.chat.id)
        if message.text.startswith("/"): return  # ignore commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if 2 < len(message.text) < 100:
            search = await replace_words(message.text)
            files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
            if not files:
                if settings["spell_check"]:
                    return await advantage_spell_chok(msg, message)
                else:
                    return
        else:
            return
    else:
        settings = await get_settings(msg.message.chat.id)
        message = msg.message.reply_to_message  # msg will be callback query
        search, files, offset, total_results = spoll
    pre = 'filep' if settings['file_secure'] else 'file'
    if settings["button"]:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'{pre}#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'{pre}_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
             [InlineKeyboardButton(text="ᴘᴀɢᴇꜱ", callback_data="pages"),
             InlineKeyboardButton(text=f"1/{round(int(total_results) / temp.multi_buttons)}", callback_data="pages"),
             InlineKeyboardButton(text="ɴᴇxᴛ ⫸", callback_data=f"next_{req}_{key}_{offset}")]
        )
    else:
        btn.append(
            [InlineKeyboardButton(text="🔘 ɴᴏ ᴍᴏʀᴇ ᴘᴀɢᴇs ᴀᴠᴀɪʟᴀʙʟᴇ 🔘", callback_data="pages")]
        )
    btn.insert(0, 
        [
            InlineKeyboardButton('ʙᴏᴛ ɪɴғᴏ', callback_data='ss_alert'),
            InlineKeyboardButton('ʀᴜʟᴇs', callback_data='rules_alert')
        ],
    )
    btn.insert(1, [
        InlineKeyboardButton("HOW TODOWNLOAD", url=malik.int_link)
    ])
    imdb = await get_poster(search, file=(files[0]).file_name) if settings["imdb"] else None
    TEMPLATE = settings['template']
    if imdb:
        cap = TEMPLATE.format(
            query=search,
            title=imdb['title'],
            votes=imdb['votes'],
            aka=imdb["aka"],
            seasons=imdb["seasons"],
            box_office=imdb['box_office'],
            localized_title=imdb['localized_title'],
            kind=imdb['kind'],
            imdb_id=imdb["imdb_id"],
            cast=imdb["cast"],
            runtime=imdb["runtime"],
            countries=imdb["countries"],
            certificates=imdb["certificates"],
            languages=imdb["languages"],
            director=imdb["director"],
            writer=imdb["writer"],
            producer=imdb["producer"],
            composer=imdb["composer"],
            cinematographer=imdb["cinematographer"],
            music_team=imdb["music_team"],
            distributors=imdb["distributors"],
            release_date=imdb['release_date'],
            year=imdb['year'],
            genres=imdb['genres'],
            poster=imdb['poster'],
            plot=imdb['plot'],
            rating=imdb['rating'],
            url=imdb['url'],
            **locals()
        )
    else:
        cap = f"<b>🖥 Movie Name : {search}\n📡Group : {message.chat.title}\nRequested By : {message.from_user.mention}</b>"
    if imdb and imdb.get('poster'):
        try:
          ab = await message.reply_photo(photo=imdb.get('poster'), caption=cap, reply_markup=InlineKeyboardMarkup(btn))
          if settings['auto_deletee']:
              await asyncio.sleep(malik.delete)
              await ab.delete()
              await message.delete()
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):  
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=imdb.get('poster'), caption=cap, reply_markup=InlineKeyboardMarkup(btn))
            if settings['auto_deletee']:
                abb = await asyncio.sleep(malik.delete)
                await abb.delete()
                await message.delete()
        except Exception as e:
            logger.exception(e)
            abbb = await message.reply_photo(photo=malik.smart_pic, caption=cap, reply_markup=InlineKeyboardMarkup(btn))
            if settings['auto_deletee']:
                await asyncio.sleep(malik.delete)
                await abbb.delete()
                await message.delete()
    else:
        abbb = await message.reply_photo(photo=malik.smart_pic, caption=cap, reply_markup=InlineKeyboardMarkup(btn))
        if settings['auto_deletee']:
             await asyncio.sleep(malik.delete)
             await abbb.delete()
             await message.delete()
    if spoll:
        await msg.message.delete()



async def advantage_spell_chok(msg, message):
    settings = await get_settings(message.chat.id)
    query = re.sub(
        r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)",
        "", msg.text, flags=re.IGNORECASE)  # plis contribute some common words
    malik = query.strip()
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        reply = malik.replace(" ", '+')  
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔍 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗖𝗵𝗲𝗰𝗸 𝗦𝗽𝗶𝗹𝗹𝗶𝗻𝗴 ✅", url=f"https://www.google.com/search?q={reply}")
        ],[
        InlineKeyboardButton("🔍 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲 𝗗𝗮𝘁𝗲 📅", url=f"https://www.google.com/search?q={reply}+release+date")
        ]]  
        )    
        a = await msg.reply_photo(
            photo=(MQTTP),
            caption=(MQTT.format(msg.from_user.mention, query)),
            reply_markup=reply_markup                 
        )
        await asyncio.sleep(100) 
        await a.delete()
        return
    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE)  # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(
        r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)',
        '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*",
                         re.IGNORECASE)  # match something like Watch Niram | Amazon Prime
        for mv in g_s:
            match = reg.match(mv)
            if match:
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed))  # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True)  # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist))  # removing duplicates
    if not movielist:
        reply = malik.replace(" ", '+')  
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔍 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗖𝗵𝗲𝗰𝗸 𝗦𝗽𝗶𝗹𝗹𝗶𝗻𝗴 ✅", url=f"https://www.google.com/search?q={reply}")
        ],[
        InlineKeyboardButton("🔍 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲 𝗗𝗮𝘁𝗲 📅", url=f"https://www.google.com/search?q={reply}+release+date")
        ]]  
        )    
        a = await msg.reply_photo(
            photo=(MQTTP),
            caption=(MQTT.format(msg.from_user.mention, query)),
            reply_markup=reply_markup                 
        )
        await asyncio.sleep(100) 
        await a.delete()
        return
    SPELL_CHECK[msg.id] = movielist
    btn = [[
        InlineKeyboardButton(
            text=movie.strip(),
            callback_data=f"spolling#{user}#{k}",
        )
    ] for k, movie in enumerate(movielist)]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spolling#{user}#close_spellcheck')])
    dll = await msg.reply(f"<b>Hey, {msg.from_user.mention}...😎\n\nᴄʜᴇᴄᴋ ᴀɴᴅ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ʟɪsᴛ.. \n\nನೀಡಿರುವ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ವೀಕ್ಷಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ👇👇👇</b>",
                    reply_markup=InlineKeyboardMarkup(btn))
    reply = malik.replace(" ", '+')
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton("🔍 Click To Check Spilling ✅", url=f"https://www.google.com/search?q={reply}")
    ],[
    InlineKeyboardButton("🔍 Click To Check Release Date📅", url=f"https://www.google.com/search?q={reply}+release+date")
    ],[
    InlineKeyboardButton("Wikipedia ⭕️", url=f"https://en.m.wikipedia.org/w/index.php?search={reply}")
    ]]
    )    
    dl = await msg.reply_photo(
        photo=(MQTTP),
        caption=(MQTT.format(msg.from_user.mention, query)),
        reply_markup=reply_markup 
    ) 
    if settings['auto_deletee']:
        await asyncio.sleep(32)
        await dl.delete()
    if settings['auto_deletee']:
        await asyncio.sleep(35)
        await dll.delete()   



async def manual_filters(client, message, text=False):
    settings = await get_settings(message.chat.id)
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await client.send_message(group_id, reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await client.send_message(
                                group_id,
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id=reply_id
                            )
                    elif btn == "[]":
                        await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id=reply_id
                        )
                    else:
                        button = eval(btn)
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id=reply_id
                        )
                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False


