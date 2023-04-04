
class script(object):
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
✯ <b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/{}>{}</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
✯ updates channel: <a href=https://t.me/filmyfunda_movies>CLICK HERE</a>""" 
    SOURCE_TXT = """<b>NOTE:</b>
- <b>Thunder is a private project.

<b>DEVS:</b>
- <a href=https://t.me/bhatmanju>jack sparrow</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. thunder bot have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- thunder bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. movies house supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/bhatmanju)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Thunder bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ <b>𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/bhatmanju>jack sparrow</a></b> """
    LOG_TEXT_G = """#NewGroup
Group = {}, {}
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    START_TXT = """<b>ʜᴇʏ {}..

ɪᴍ ⚡️ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ʙᴏᴛ...
😎 ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴀs ᴀ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ....
ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ: ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ, ᴛʜᴀᴛs ᴀʟʟ, ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ...😎

⚠️ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ..

©ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ: jack sparrow</b>"""

    MALIK_TXT =  """<b>Donation</b>

<b>Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive...</b>


⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺           
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲     
✮ 𝗣𝗮𝘆𝗣𝗮𝗹

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/bhatmanju><b>jack sparrow</b></a> ᚛━━━━━━━━━━━━"""
    DINETTE_TXT =  """<b>Donation</b>


<b>Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive...</b>


⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺           
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲     
✮ 𝗣𝗮𝘆𝗣𝗮𝗹

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/bhatmanju><b>jack sparrow</b></a> ᚛━━━━━━━━━━━━"""
    VIDEO_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
/𝘮𝘱4 https://youtu.be/Your Link<\b>"""

    VIDEOS_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
/𝘮𝘱4 https://youtu.be/Your Link<\b>"""

    YTTHUMB_TXT = """<b>𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
/ytthumb https://youtu.be/yourlink</b>"""

    FORCESUB_TXT = """⚠️ Join our updated channel below.  bot will not give you movie until you join from our update channel...
    
⚠️ ಕೆಳಗಿನ ನಮ್ಮ  ಚಾನಲ್‌ಗೆ ಸೇರಿ. ನಮ್ಮ ಅಪ್‌ಡೇಟ್ ಚಾನೆಲ್‌ಗೆ ನೀವು ಸೇರುವವರೆಗೆ ಬೋಟ್ ನಿಮಗೆ ಚಲನಚಿತ್ರವನ್ನು ನೀಡುವುದಿಲ್ಲ
ಆದ್ದರಿಂದ ಮೊದಲು ಈ ಚಾನೆಲ್ ಅನ್ನು ಸೇರಿ...

⚠️ கீழே உள்ள எங்கள் புதுப்பிக்கப்பட்ட சேனலில் சேரவும்.  எங்கள் புதுப்பிப்பு சேனலில் நீங்கள் சேரும் வரை போட் உங்களுக்கு திரைப்படத்தை வழங்காது... 

⚠️ ചുവടെയുള്ള ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചെയ്‌ത ചാനലിൽ ചേരുക.  ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചാനലിൽ നിന്ന് നിങ്ങൾ ചേരുന്നത് വരെ ബോട്ട് നിങ്ങൾക്ക് സിനിമ നൽകില്ല....

⚠️ हमारे निचे दिए गये update चैनल को join करे जब तक आप हमारे update चैनल को join नहीं करेंगे तब तक bot आपको मूवी नहीं देगा..."""

    URLSHORT_TXT = """<b>➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/short https://t.me/+veUIdIW2CQ5GU5</b>"""


    URLSHORTN_TXT = """<b>➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/short https://t.me/+veUIdIW25mOGU5</b>"""

    GHHM_TXT = """<b>7k User 💖 Thanks For Your Support...

𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖮𝗎𝗋 𝖡𝗈𝗍 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 𝖨𝗍 𝖶𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾... 😎


     ♋️ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 ♋️

✪ AutoFilter, Manual Filter
✪ IMDb HD Posters
✪ IMDb Real Details
✪ Two Buttons Mode
✪ Force Subscribe
✪ Extra Features: download songs, download you tube video, URL Shortner,  

⚙ More Features Adding Soon</b> 😎"""

    GHHN_TXT = """Extra features"""

    OWNER_TXT = """<b>>━━━━᚜ Owner Details ᚛━━━━<
    
⭕️ FULL NAME : jack sparrow
⭕️ USERNAME: @bhatmanju
⭕️PERMANENT DM LINK : <a href=https://t.me/bhatmanju>CLICK Here</a></b>"""

    SPELLING_TEXT = """<u><b> jack sparrow </b></u>"""


    GROUP_R_TXT = """<b>GROUP RULES

☀️  Search With Correct Spelling..

☀️ Try to Search movie With  Year If The bot is Not Sending You Accurate Result..

☀️ Search Series In The Given From Example : Gotham S03E01 And S03E10..

☀️ Search Movies  in The Given From Example:    
(1) Avengers.. ✅
(2) Avengers Hindi. ✅
(3) Don't Tipe Avengers Hindi Dubbed..❌

☀️Don't Do Any Self Promotion.

☀️ Don't Send Any Kind Of Photo Video Documents URL ETC.

☀️ Sending The Above  Mantained Things Will Lead To Permanent Ban.

☀️Don't Request Any Things Other Than Movie Series Animes.

☀️ Give and Take Respect</b>.."""

MALIK_PHH = """<b>Hay 👋 {}.... 🌷 ❤️

😎 welcome to Our Group...
  
        😎 👉 <s>{}</s> 👈 😎

😎 You Can Find 🔍 Movies / Series / Animes etc. From Here. Enjoy 😉...

🙏 Plz do You not request the owner for the movie.. or else you will be blocked directly...⚠️

⚙ If there is any problem with the bot then contact the owner..

If you have any question then contact us below  👇</b>"""

ALURT_FND = """<b>Your 👉 {}❗️ spelling is not correct, please choose from the list given 👇
 ┏━━━━•❅•°•❈•°•❅━━━━┓
 ✰ CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE..
 
 ✰ ನೀಡಿರುವ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ

 ✰ दी गई सूची में अपनी फिल्म देखें और अपनी फिल्म चुनें</b> 👇👇👇                                             ✰
 ┗━━━━•❅•°•❈•°•❅•━ ━━┛
"""

MNTFN = """<b>⭕️ ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ᴀᴅᴍɪɴ..

⭕️ ಈ ಚಲನಚಿತ್ರವು ನನ್ನ ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ ಕಂಡುಬಂದಿಲ್ಲ. Admin ಗೆ ವಿನಂತಿಸಿ

⭕️ ʏᴇ ᴍᴏᴠɪᴇ ʜᴀᴍᴀʀᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ᴍᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ɴᴀʜɪ ʜᴀɪ ɴɪᴄʜᴇ ᴀᴅᴍɪɴ ꜱᴇ ʀᴇǫᴜᴇꜱᴛ ᴋᴀʀᴇ... 

⭕️ ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ᴀᴅᴍɪɴ.. 👇</b>"""


ADG = """<b>Hay. {}..\n\nThankyou For Adding Me In.. ❣️

             👉 <s>{}</s> 👈 

If you have any questions & doubts about using me..\n\n Contact my Owner >> <a href=https://t.me/{}>Owner</a> </b>"""

ADDG = """ʜᴇʏ..

ɪᴍ ⚡️ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ʙᴏᴛ...
😎 ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴀs ᴀ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ....
ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ: ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ, ᴛʜᴀᴛs ᴀʟʟ, ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ...😎

⚠️ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ..

©ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ: filmyfunda movies"""

M_NNT_FND = """malik"""

M_NNT_FNDD = """malikb"""


