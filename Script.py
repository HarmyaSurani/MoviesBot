import os


class script(object):
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
✯ <b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/{}>{}</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: LINODE
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
✯ updates channel: <a href=https://t.me/FilmyBagNetwork>CLICK HERE</a>""" 
    SOURCE_TXT = """<b>NOTE :</b>
- <b>FilmyBag Is A Private Bot.

<b>DEVS :</b>
- <a href=https://t.me/harmya>Harmya Surani</a>"""
    MANUELFILTER_TXT = """Help : <b>Filters</b>

- Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And FilmyBag Bot Will Respond Whenever A Keyword Is Found The Message.

<b>NOTE :</b>
1. FilmyBag Bot Have Admin Privillage.
2. Only Admins Can Add Filters In A Chat.
3. Alert Buttons Have A Limit Of 64 Characters.

<b>Commands And Usage :</b>
• /filter - <code>Add A Filter In Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat (Chat Owner Only)</code>"""
    BUTTON_TXT = """Help : <b>Buttons</b>

- FilmyBag Bot Supports Both Url And Alert Inline Buttons.

<b>NOTE :</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. Movies House Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed As Markdown Format.

<b>URL Buttons :</b>
<code>[Button Text](buttonurl:https://t.me/harmya)</code>

<b>Alert Buttons :</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help : <b>Auto Filter</b>

<b>NOTE :</b>
1. Make Me The Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains Camrips, Porn And Fake Files.
3. Forward The Last Message To Me With Quotes.
 I'll Add All The Files In That Channel To My DB."""
    CONNECTION_TXT = """Help : <b>Connections</b>

- Used To Connect Bot To PM For Managing Filters. 
- It Helps To Avoid Spamming In Groups.

<b>NOTE :</b>
1. Only Admins Can Add A Connection.
2. Send <code>/connect</code> For Connecting Me To Ur PM.

<b>Commands And Usage :</b>
• /connect  - <code>Connect A Particular Chat To your PM</code>
• /disconnect  - <code>Disconnect From A chat</code>
• /connections - <code>List All Your Connections</code>"""
    EXTRAMOD_TXT = """Help : <b>Extra Modules</b>

<b>NOTE :</b>
- These Are The Extra Features Of FilmyBag Bot.

<b>Commands and Usage :</b>
• /id - <code>Get Id Of A Specified User</code>
• /info  - <code>Get Information About A User</code>
• /imdb  - <code>Get The Film Information From IMDb Source</code>
• /search  - <code>Get The Film Information from Various Sources</code>"""
    ADMIN_TXT = """Help : <b>Admin Mods</b>

<b>NOTE :</b>
This Module Only Works For My Admins

<b>Commands and Usage :</b>
• /logs - <code>To Get The Rescent Errors</code>
• /stats - <code>To Get Status Of Files In DB</code>
• /delete - <code>To Delete A Specific File From DB</code>
• /users - <code>To Get List Of My Users And Ids</code>
• /chats - <code>To Get List Of The My Chats And Ids </code>
• /leave  - <code>To Leave From A Chat</code>
• /disable  -  <code>To Disable A Chat</code>
• /ban  - <code>To Ban A User</code>
• /unban  - <code>To Unban A User</code>
• /channel - <code>To Get List Of Total Connected Channels</code>
• /broadcast - <code>To Broadcast A Message To All Users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 : <code>{}</code>
★ <b>𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂 : <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂 : <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 : <code>{}</code> 𝙼𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 : <code>{}</code> 𝙼𝙱
★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href=https://t.me/harmya>Harmya Surani</a></b> """
    LOG_TEXT_G = """#NewGroup
Group = {}, {}
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    START_TXT = """<b>Hey {}..

I Am A⚡️ POWERFUL AUTOFILTER BOT...
😎 You Can Use Me As A Auto-Filter In Your Group....
It's Easy To Use Me : Just Add Me To Your Group As Admin, That's All, I Will Provide Movies There....

⚠️ FOR MORE HELP CHECK HELP BUTTON

©MAINTAINED BY : @FilmyBagNetwork</b>"""

    MALIK_TXT =  """<b>Donation</b>

<b>Developer Is Super Noob. Just Learning From Official Docs. Please Donate The Developer For Keeping The Service Alive...</b>


⪼ <b>You Can Donate Any Amount You Have</b>

<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ UPI
✮ Paytm           
✮ PhonePe     
✮ PayPal
✮ Airtm
✮ Skrill
✮ Payeer

_Contact Me To Know About The Payment Info_
━━━━━━━━━━━━᚜ <a href=https://t.me/harmya><b>Harmya Surani</b></a> ᚛━━━━━━━━━━━━"""
    DINETTE_TXT =  """<b>Donation</b>


<b>Developer Is Super Noob. Just Learning From Official Docs. Please Donate The Developer For Keeping The Service Alive...</b>


⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞</b>

<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ UPI
✮ Paytm           
✮ PhonePe     
✮ PayPal
✮ Airtm
✮ Skrill
✮ Payeer

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/harmya><b>Harmya Surani</b></a> ᚛━━━━━━━━━━━━"""
    VIDEO_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 ANY 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

⭕ 𝘜𝘴𝘢𝘨𝘦 :
- 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 :
- 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
- 𝘌𝘹𝘢𝘮𝘱𝘭𝘦 : /𝘮𝘱4 https://youtu.be/Your Link<\b>"""

    VIDEOS_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 MULTIPLE 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 VIDEOS

⭕ 𝘜𝘴𝘢𝘨𝘦 :
- 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 Multiple 𝘝𝘪𝘥𝘦𝘰es 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 :
- 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Links)
- 𝘌𝘹𝘢𝘮𝘱𝘭e : /𝘮𝘱4 https://youtu.be/Your1 https://youtu.be/Your2
- 𝘌𝘹𝘢𝘮𝘱𝘭e : /video https://youtu.be/Your1 https://youtu.be/Your2<\b>"""

    YTTHUMB_TXT = """<b>𝙷𝙴𝙻𝙿 YOU 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕ 𝘜𝘴𝘢𝘨𝘦 :
- 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘠𝘰𝘶𝘵𝘶𝘣𝘦 Video Thumbnail

⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 :
- 𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦 : /ytthumb https://youtu.be/yourlink</b>"""

    FORCESUB_TXT = """⚠️ Join Our Updated Channel Below.  Bot Will Not Give You Movie Until You Join From Our Update Channel....
    
⚠️ ಕೆಳಗಿನ ನಮ್ಮ  ಚಾನಲ್‌ಗೆ ಸೇರಿ. ನಮ್ಮ ಅಪ್‌ಡೇಟ್ ಚಾನೆಲ್‌ಗೆ ನೀವು ಸೇರುವವರೆಗೆ ಬೋಟ್ ನಿಮಗೆ ಚಲನಚಿತ್ರವನ್ನು ನೀಡುವುದಿಲ್ಲ
ಆದ್ದರಿಂದ ಮೊದಲು ಈ ಚಾನೆಲ್ ಅನ್ನು ಸೇರಿ....

⚠️ கீழே உள்ள எங்கள் புதுப்பிக்கப்பட்ட சேனலில் சேரவும்.  எங்கள் புதுப்பிப்பு சேனலில் நீங்கள் சேரும் வரை போட் உங்களுக்கு திரைப்படத்தை வழங்காது.... 

⚠️ ചുവടെയുള്ള ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചെയ്‌ത ചാനലിൽ ചേരുക.  ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചാനലിൽ നിന്ന് നിങ്ങൾ ചേരുന്നത് വരെ ബോട്ട് നിങ്ങൾക്ക് സിനിമ നൽകില്ല....

⚠️ हमारे निचे दिए गये Update चैनल को Join करे जब तक आप हमारे Update चैनल को Join नहीं करेंगे तब तक Bot आपको मूवी नहीं देगा...."""

    URLSHORT_TXT = """<b>➤ 𝐇𝐞𝐥𝐩 : 𝖴𝗋𝗅 S𝗁𝗈𝗋𝗍e𝗇𝖾𝗋

⭕  Usage :
- 𝚃𝚑𝚒𝚜 C𝚘𝚖𝚖𝚊𝚗𝚍 H𝚎𝚕𝚙𝚜 Y𝚘𝚞 T𝚘 Sh𝚘𝚛𝚝 A U𝚛𝚕 

⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 :
- U𝗌𝖾 /short C𝗈𝗆𝗆𝖺𝗇𝖽 W𝗂𝗍𝗁 Y𝗈𝗎𝗋 L𝗂𝗇𝗄 T𝗈 G𝖾𝗍 S𝗁𝗈𝗋𝗍𝖾𝖽 L𝗂𝗇𝗄𝗌 With Your Link Shortener

• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : /short https://google.com</b>"""


    URLSHORTN_TXT = """<b> Help : 𝖴𝗋𝗅 S𝗁𝗈𝗋𝗍e𝗇𝖾𝗋

⭕  Usage :
- 𝚃𝚑𝚒𝚜 C𝚘𝚖𝚖𝚊𝚗𝚍 H𝚎𝚕𝚙𝚜 Y𝚘𝚞 T𝚘 S𝚑𝚘𝚛𝚝 A U𝚛𝚕 

⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 :
- U𝗌𝖾 /short C𝗈𝗆𝗆𝖺𝗇𝖽 W𝗂𝗍𝗁 Y𝗈𝗎𝗋 L𝗂𝗇𝗄 T𝗈 G𝖾𝗍 S𝗁𝗈𝗋𝗍𝖾𝖽 L𝗂𝗇𝗄𝗌 With Your Link Shortener

• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : /short https://google.com</b>"""

    GHHM_TXT = """<b>💖 Thanks For Your Support...

𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖮𝗎𝗋 𝖡𝗈𝗍 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 𝖨𝗍 𝖶𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾... 😎


     ♋️ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 ♋️

✪ AutoFilter, Manual Filter
✪ IMDb HD Posters
✪ IMDb Real Details
✪ Two Buttons Mode
✪ Force Subscribe
✪ Extra Features: Download Youtube Video Thumbnail, Download YouTube Videoes, URL Shortener  

⚙ More Features Adding Soon</b> 😎"""

    GHHN_TXT = """Extra Features"""

    OWNER_TXT = """<b>>━━━━᚜ Owner Details ᚛━━━━<
    
⭕️ FULL NAME : Harmya Surani
⭕️ USERNAME: @harmya
⭕️ PERMANENT DM LINK : <a href=https://t.me/harmya>Click Here</a></b>"""

    SPELLING_TEXT = """<u><b> Harmya Surani </b></u>"""


    GROUP_R_TXT = """<b>⭕️ GROUP RULES :

☀️  Search With Correct Spelling..

☀️ Try To Search Movie With Year If The Bot Is Not Sending You Accurate Result.

☀️ Search Series In The Given From Example : Gotham S03E01 And S03E10.

☀️ Search Movies  in The Given From Example :    
(1) Avengers.. ✅
(2) Avengers Hindi.. ✅
(3) Don't Type Avengers Hindi Dubbed.. ❌

☀️ Don't Do Any Self Promotion.

☀️ Don't Send Any Kind Of Photo Video Documents URL ETC.

☀️ Sending The Above  Mantained Things Will Lead To Permanent Ban.

☀️ Don't Request Any Things Other Than Movie Series Animes.

☀️ Give And Take Respect</b>"""

MALIK_PHH = """<b>Hay 👋 {}.... 🌷 ❤️

😎 Welcome To FilmyBag Group...
  
        😎 👉 <s>{}</s> 👈 😎

😎 You Can Find 🔍 Movies / Series / Animes Etc. From Here. Enjoy 😉

⚙ If There Is Any Problem With The Bot Then Contact The Owner.

👉 If You Have Any Question Then Contact Us Below  👇</b>"""

ALURT_FND = """<b>Your 👉 {}❗️ Spelling Is Not Correct, Please Choose From The List Given 👇
 ┏━━━━•❅•°•❈•°•❅━━━━┓
 ✰ CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE...
 
 ✰ ನೀಡಿರುವ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಚಲನಚಿತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ...

 ✰ दी गई सूची में अपनी फिल्म देखें और अपनी फिल्म चुनें...</b> 👇👇👇                                             ✰
 ┗━━━━•❅•°•❈•°•❅•━ ━━┛
"""

MNTFN = """<b>⭕️ THIS MOVIE IS NOT AVAILABLE IN MY DATABASE. REQUEST TO ADMIN....

⭕️ ಈ ಚಲನಚಿತ್ರವು ನನ್ನ ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ ಕಂಡುಬಂದಿಲ್ಲ. Admin ಗೆ ವಿನಂತಿಸಿ....

⭕️ YE MOVIE HAMARE DATABASE ME NAHI HE ADMIN SE REQUEST KARE....

⭕️ REQUEST TO ADMIN HERE 👇</b>"""


ADG = """<b>Hay. {}..\n\nThank You For Adding Me In.. ❣️

             👉 <s>{}</s> 👈 

👉 If You Have Any Questions & Doubts About Using Me..\n Contact My Owner >> <a href=https://t.me/{}>Harmya Surani</a> </b>"""

ADDG = """👋 Hey ..

I Am ⚡️ Powerful Auto-Filter Bot.
😎 You Can Use Me As A Auto-Filter In Your Group.
It's Easy To Use Me : Just Add Me To Your Group As Admin, That's All, I Will Provide Movies There...😎

⚠️ For More Help Check Help Button

©Maintain By : FilmyBag Network"""

M_NNT_FND = """malik"""

M_NNT_FNDD = """malikb"""

MALIK2 = """#verification_1

<b>Hay</b> {} !

You Are Not Verified Today. Tap On The Verify 🔗Link And Get Unlimited Access For Whole ⌛️Day.\n\n<bइस बॉट को इस्तेमाल करने के लिए आपको रोजाना 1 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे</b>"""

SECOND_VERIFICATION_TEXT = """#verification 2

<b>Hay {} !

You Are Not Verified Today. Tap On The Verify 🔗Link And Get Unlimited Access For Whole ⌛️Day.\n\n<bइस बॉट को इस्तेमाल करने के लिए आपको रोजाना 1 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे</b>"""

SECOND_VERIFICATION_TEXT = os.environ.get('SECOND_VERIFICATION_TEXT', SECOND_VERIFICATION_TEXT)


MALIK7 = """Hay {}!

You Have Completed The Verification, Now You Can Get Unlimited Access For Whole Day.\n\nPlease Join My Main Channel 👇"""



SECOND_VERIFY_COMPLETE_TEXT = """Hay {}!

You Have Completed The Verification, Now You Can Get Unlimited Access For Whole Day.\n\nPlease Join My Main Channel 👇"""



