from datetime import datetime
import string
import os
import logging
import random
import asyncio
import pytz
from plugins import malik
from plugins.malik2.buttons import GSLB
from Script import script, ADDG, MALIK2, SECOND_VERIFICATION_TEXT, SECOND_VERIFY_COMPLETE_TEXT, MALIK7
from pyrogram import Client, filters, enums 
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id, get_del_files
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, PHTT, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT, REQ_GRP, MALIK, MALIK5, TUTORIAL_LINK_1, TUTORIAL_LINK_2
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp, get_shortlink
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}
quote = {}


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client:Client, message):
    
    m = message
    user_id = m.from_user.id

    if len(m.command) == 2 and m.command[1].startswith('notcopy'):
        user_id = int(m.command[1].split("_")[1])
        verify_id = m.command[1].split("_")[2]

        verify_id_info = await db.get_verify_id_info(user_id, verify_id)
        if not verify_id_info or verify_id_info["verified"]:
            await message.reply("Invalid link. Link has already verified or has wrong hash. Try Again")
            return

        ist_timezone = pytz.timezone('Asia/Kolkata')
        
        key = "second_time_verified" if await db.is_user_verified(user_id) else "last_verified"
        
        await db.update_notcopy_user(user_id, {key:datetime.now(tz=ist_timezone)})
        await db.update_verify_id_info(user_id, verify_id, {"verified":True})

        text = f"""User ID : `{user_id}`
Username : {m.from_user.mention}
Time : {datetime.now(tz=ist_timezone).strftime('%Y-%m-%d %H:%M:%S')}

#New_Verified_User_complete"""
        txt = SECOND_VERIFY_COMPLETE_TEXT if key == "second_time_verified" else MALIK7
        await client.send_message(LOG_CHANNEL, text)
        dmm = await m.reply_photo(
        photo=(MALIK5), 
        caption=(txt.format(message.from_user.mention)), 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶 Back to Group 🚶",url="https://t.me/+GA9ku5KyDGFiMzVl"),]]),parse_mode=enums.ParseMode.HTML)#"You are now verified for next 24 hours. Continue asking movies")
        return

    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        reply_markup = malik.hstnn
        await message.reply_text(
        text=(ADDG.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME)),
        reply_markup=reply_markup)
        await asyncio.sleep(2) 
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        reply_markup = malik.hstn
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "👉 Join Updates Channel 👈", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            kk, file_id = message.command[1].split("_", 1)
            pre = 'checksubp' if kk == 'filep' else 'checksub' 
            btn.append([InlineKeyboardButton("♻️ Try Again ♻️", callback_data=f"{pre}#{file_id}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text=script.FORCESUB_TXT,
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        reply_markup = malik.hstn
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    # User Verifying
    user_id = m.from_user.id

    user_verified = await db.is_user_verified(user_id)
    is_second_shortener = await db.use_second_shortener(user_id)

    how_to_download_link = TUTORIAL_LINK_2 if is_second_shortener else TUTORIAL_LINK_1
    
    if not user_verified or is_second_shortener:
        verify_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        await db.create_verify_id(user_id, verify_id)
        buttons = [[InlineKeyboardButton(text="🔹 Click hare to Verify 🔹", url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=notcopy_{user_id}_{verify_id}", is_second_shortener),),], [InlineKeyboardButton(text="🌀 How to verify 🌀", url=how_to_download_link)]]
        reply_markup=InlineKeyboardMarkup(buttons)
        num = 2 if is_second_shortener else 1

        text = f"""User ID : `{user_id}`
Username : {m.from_user.mention}
Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

#New_Verify_{num}_User"""
        await client.send_message(LOG_CHANNEL, text)
        bin_text = SECOND_VERIFICATION_TEXT if is_second_shortener else MALIK2
        dmb = await m.reply_text(
            #photo=(MALIK), #caption=(MALIK2)),
            text=(bin_text.format(message.from_user.mention)),
            protect_content = True,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(120) 
        await dmb.delete()
        return


    if data.split("-", 1)[0] == "BATCH":
        sts = await message.reply("Please wait")
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if BATCH_FILE_CAPTION:
                try:
                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            try:
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
            await asyncio.sleep(1) 
        await sts.delete()
        return
    elif data.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("Please wait")
        b_string = data.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        try:
            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)
        except:
            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
            protect = "/pbatch" if PROTECT_CONTENT else "batch"
        diff = int(l_msg_id) - int(f_msg_id)
        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):
            if msg.media:
                media = getattr(msg, msg.media)
                if BATCH_FILE_CAPTION:
                    try:
                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))
                    except Exception as e:
                        logger.exception(e)
                        f_caption = getattr(msg, 'caption', '')
                else:
                    media = getattr(msg, msg.media)
                    file_name = getattr(media, 'file_name', '')
                    f_caption = getattr(msg, 'caption', file_name)
                try:
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            elif msg.empty:
                continue
            else:
                try:
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            await asyncio.sleep(1) 
        return await sts.delete()
        

    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=True if pre == 'filep' else False,
                )
            filetype = msg.media
            file = getattr(msg, filetype)
            title = file.file_name
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(f_caption)
            return
        except:
            pass
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    dil = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=True if pre == 'filep' else False,
        reply_markup=GSLB,
    )
    await asyncio.sleep(290)
    await dil.delete()

  
@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return
    
    file_id, file_ref = unpack_new_file_id(media.file_id)

    result = await Media.collection.delete_one({
        '_id': file_id,
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_many({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            await msg.reply_sticker("CAACAgQAAxkBAAEMG15jDjwsk8k-5cTwbT-z8PskMc8f4wAClAoAAsxaMVH2n5EFnEtBnx4E")
            await msg.edit('File is successfully deleted from database')
        else:
            # files indexed before https://github.com/EvamariaTG/EvaMaria/commit/f3d2a1bcb155faf44178e5d7a685a1b533e714bf#diff-86b613edf1748372103e94cacff3b578b36b698ef9c16817bb98fe9ef22fb669R39 
            # have original file name.
            result = await Media.collection.delete_many({
                'file_name': media.file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                await msg.edit('File is successfully deleted from database')
            else:
                await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer('Piracy Is Crime')
    await message.message.edit('Succesfully Deleted All The Indexed Files.')


@Client.on_message(filters.command('settings'))
async def settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return
    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != enums.ChatMemberStatus.ADMINISTRATOR
            and st.status != enums.ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return
    
    settings = await get_settings(grp_id)

    if settings is not None:
        buttons = [
            [      
                InlineKeyboardButton(
                    'Filter button',
                    callback_data=f'setgs#button#{settings["button"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    'Single' if settings["button"] else 'Double',
                    callback_data=f'setgs#button#{settings["button"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Bot PM',
                    callback_data=f'setgs#botpm#{settings["botpm"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Yes' if settings["botpm"] else '❌ No',
                    callback_data=f'setgs#botpm#{settings["botpm"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'File Secure',
                    callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Yes' if settings["file_secure"] else '❌ No',
                    callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'IMDB',
                    callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Yes' if settings["imdb"] else '❌ No',
                    callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Spell Check',
                    callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Yes' if settings["spell_check"] else '❌ No',
                    callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Welcome msg',
                    callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ Yes' if settings["welcome"] else '❌ No',
                    callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Spell Auto Delete',
                    callback_data=f'setgs#spell_auto_delete#{settings["spell_auto_delete"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ ON' if settings["spell_auto_delete"] else '❌ OFF',
                    callback_data=f'setgs#spell_auto_delete#{settings["spell_auto_delete"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Manual Filter',
                    callback_data=f'setgs#manual_filter#{settings["manual_filter"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ ON' if settings["manual_filter"] else '❌ OFF',
                    callback_data=f'setgs#manual_filter#{settings["manual_filter"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Movies Auto Delete',
                    callback_data=f'setgs#auto_deletee#{settings["auto_deletee"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ ON' if settings["auto_deletee"] else '❌ OFF',
                    callback_data=f'setgs#auto_deletee#{settings["auto_deletee"]}#{grp_id}',
                ),
            ],
            [
                InlineKeyboardButton(
                    'Auto Filter',
                    callback_data=f'setgs#auto_filters#{settings["auto_filters"]}#{grp_id}',
                ),
                InlineKeyboardButton(
                    '✔ ON' if settings["auto_filters"] else '❌ OFF',
                    callback_data=f'setgs#auto_filters#{settings["auto_filters"]}#{grp_id}',
                ),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply_text(
            text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML,
            reply_to_message_id=message.id
        )

@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    sts = await message.reply("Checking template")
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != enums.ChatMemberStatus.ADMINISTRATOR
            and st.status != enums.ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return

    if len(message.command) < 2:
        return await sts.edit("No Input!!")
    template = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'template', template)
    await sts.edit(f"Successfully changed template for {title} to\n\n{template}")


@Client.on_message(filters.command('pm') & filters.channel)
async def message_cmd_handler(client: Client, m: Message):
    try:
        if len(m.command) < 4:
            wrong_input_txt = "Use this format to send message: `/pm user_id msg_id message`"
            return await m.reply(wrong_input_txt)

        user_id = int(m.command[1])
        reply_msg_id = int(m.command[2])

        try:
            user_mention = (await client.get_users(user_id)).mention
        except Exception as e:
            await m.reply("Some error occurred while fetching user information. Maybe user didn't start the bot yet")
            return 
            
        text = f'Dear {user_mention}, You have a message from admin\n\n{m.text.replace(f"/pm {user_id} {reply_msg_id} ", "")}'
        await client.send_message(REQ_GRP, text, reply_to_message_id=reply_msg_id)
    except Exception as e:
        print(e)


@Client.on_message(filters.command("del_files") & filters.private & filters.user(ADMINS))
async def del_files(bot, message): 
    msg = message
    chats = msg.chat.type
    if chats != enums.ChatType.PRIVATE:
        return await msg.reply_text(f"<b>Hey {msg.from_user.mention}, This command only works on my PM !</b>")
    else:
        pass
    try:
        keyword = msg.text.split(" ", 1)[1]
    except:
        return await msg.reply_text(f"<b>Hey {msg.from_user.mention}, Give me a keyword along with the command to delete files.</b>")
    k = await bot.send_message(chat_id=msg.chat.id, text=f"<b>Fetching Files for your query {keyword} on my DB... Please wait...</b>")
    files, next_offset, total = await get_del_files(keyword)
    await k.edit_text(f"<b>Found {total} files for your query {keyword} !</b>")
    deleted = 0
    for file in files:
        file_ids = file.file_id
        file_name = file.file_name
        result = await Media.collection.delete_one({
            '_id': file_ids,
        })
        if result.deleted_count:
            logger.info(f'File Found for your query {keyword}! Successfully deleted {file_name} from database.')
        deleted += 1
    deleted = str(deleted)
    await k.edit_text(text=f"<b>Successfully deleted {deleted} files from database for your query {keyword}.</b>")

