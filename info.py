import os, re
from os import environ

from dotenv import load_dotenv
load_dotenv()

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '5363773'))
API_HASH = environ.get('API_HASH', '0433df559c3256e881f48a19171a80b8')
BOT_TOKEN = environ.get('BOT_TOKEN', '6117770218:AAFZlIi4CDkmd7vvcc_Y52zTA_fEI6scRMU')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))


# test 
DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())



PICS = (environ.get('PICS', 'https://i.postimg.cc/Px9hMgKy/PICS.png')).split()
MALIK_PH = environ.get("MALIK_PH", "https://i.postimg.cc/tTYpWqd7/MALIK-PH.png")
SMART_PIC = environ.get("SMART_PIC", "https://i.postimg.cc/XvNVNcpf/SMART-PIC.png")
VIDEO_VD = environ.get("VIDEO_VD", "https://telegra.ph/file/566ff238e36d9f2425568.mp4")
M_N_F = environ.get("M_N_F", "https://i.postimg.cc/XYbjm0WD/M-N-F.png")
PHT = environ.get("PHT", "https://i.postimg.cc/wBW91ymS/PHT.png")
PHTT = environ.get("PHTT", "https://telegra.ph/file/1ddc551c64a4afd5a660e.mp4")
M_NT_F = environ.get("M_NT_F", "https://i.postimg.cc/4ycG2WSg/M-NT-F.png")

DEL_SECOND = int(os.environ.get("DEL_SECOND", "500"))


CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "harmya")
CREATOR_NAME = os.environ.get("CREATOR_NAME", "Harmya Surani")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "FilmyBagBot")


auth_userss = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERSS', '').split()]
AUTH_USERSS = (auth_userss) if auth_userss else []

AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE2 = is_enabled((environ.get('AUTO_DELETE2', "True")), True)
# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1446498316 5923734107').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001785157194').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001885679140')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://filmybagin:GUN07gun07@filmybag.bc78ldn.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "FilmyBag")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


# Others
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "5")
DB_AUTO_DELETE = is_enabled((environ.get('DB_AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001821281332'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'FilmyBagAdmin')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
                                  
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 <b>Title</b>: <a href={url}>{title}</a>\n🎭<b> 𝐆𝐞𝐧𝐫𝐞𝐬​</b>: {genres}</a>\n📆 <b>𝐘𝐞𝐚𝐫​</b>: <a href={url}/releaseinfo>{year}</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

REQ_GRP = int(environ.get('REQ_GRP', '-1001830894693'))
RQST_CHANNEL = int(environ.get('RQST_CHANNEL', '-1001885679140'))



SHORTENER_API = environ.get("SHORTENER_API", "YfbBJnumldXUva78VgOhwGNXmju2")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shareus.io")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")

SHORT_URL = is_enabled((environ.get('SHORT_URL', "True")), True)
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://youtu.be/Jl045VfNk28")

MALIK = environ.get("malik", "https://i.postimg.cc/2j98FFYc/MALIK.png")
MALIK5 = environ.get("malik5", "https://i.postimg.cc/gj7zzd4F/MALIKS.png")

TUTORIAL_LINK_2 = os.environ.get('TUTORIAL_LINK_2', 'https://youtu.be/Jl045VfNk28')
TUTORIAL_LINK_1 = os.environ.get('TUTORIAL_LINK_1', 'https://youtu.be/Jl045VfNk28')

BLACKLIST_WORDS=["none"]


