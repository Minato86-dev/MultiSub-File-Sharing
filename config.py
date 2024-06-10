#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "1949389"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b6866140cf6064d6c27de44915015879")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001766230079"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1308086294"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hshhentai:hshhentai@cluster0.vhi4kjp.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002145190977"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002241322609"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#token varibles
# my shortner https://dashboard.shareus.io/signup/lifetime/U9AZbV

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "exe.io")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "9080a6eaa8370741a097a770e17e7262f1881190")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 2592000)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://youtu.be/pQ6G5wi1tWA?")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇʀ ʙᴏᴛ ᴏꜰ ɪᴀꜱ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ, ɪ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ ɪɴꜱɪᴅᴇ ᴍᴇ ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴛʜᴇᴍ ʙʏ ꜱᴏʟᴠɪɴɢ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰʀᴏᴍ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ! » @IAS_MOVIESANDSERIES</b>")
try:
    ADMINS=[1308086294]
    for x in (os.environ.get("ADMINS", "1308086294").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Sorry {first), You Are Not Joined In Our Channles, In Order To Access Files You Must Be Joined In The Channel...\n\n Kindly Please Join Our Channels First Ans Then Click On "Now Click Here" Button...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @IAS_MOVIESANDSERIES</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Nigha ! You Ain't My Owner!!\n\n» My Owner : @Minato2op"

ADMINS.append(OWNER_ID)
ADMINS.append(1308086294)

LOG_FILE_NAME = "codeflixbots.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
