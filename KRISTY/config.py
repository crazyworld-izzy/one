import json
import os


def get_user_list(config, key):
    with open("{}/KRISTY/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
     
    API_ID = 18641113  # integer value, dont use "" this sign get it form my.telegram.org
    API_HASH = "bc5fea81e7bf9f3c0784a0a7d35f9c71" # get it form my.telegram.org
    TOKEN = "5864142861:AAHRGgDQnqDoWaHhP0k_ginuFMpeuDBmrPk"  # get it form @botfather.
    OWNER_ID = 5323266323  # got to @miss_kristy_bot and type /id
    OWNER_USERNAME = "kassim_darlzzz" # your telegram username
    ALLOW_CHATS = True # leave it as it is
    BOT_USERNAME = "WizkhalifaBot" # your bot username get it form @botfather
    SUPPORT_CHAT = "WizkhalifaSupport"  # Your own group for support, do not add the @ if you dont have leave it as it is
    UPDATES_CHANNEL = "Wizkhalifachannel"  # Your own chsnnel for support, do not add the @ if you dont have leave it as it is
    JOIN_LOGGER =  (
        -1001720434107
    )  # add @miss_kristy_bot in your group and type /id
    EVENT_LOGS = (
        -1001720434107
    )  # add @miss_kristy_bot in your group and type /id
    ERROR_LOG = (
        -1001720434107
    )  # add @miss_kristy_bot in your group and type /id
    STRICT_GMUTE = True #to allow gmutes
    START_STICKER = "" #sticker id for start animation
    TEMP_DOWNLOAD_DIRECTORY = ". /" # dont change
    OPENWEATHERMAP_ID = None



    # RECOMMENDED
    STRING_SESSION ="1AZWarzkBu34tmJxAa4d7zfCEKkVT9O6kFj32FrodqKoHhUNqq1O-A7FNu9sbjLt-0n4yQPQiXr_0FBnBlfJHbluYJtnl2u2HkQF_XpHLgwF8dLRLpx9D-4bum96ae_oIhm8ZovssjXNplZtzI-KoLJ6OP6Vce6XWMF1UaA6bjuxpgWLYNBzI-NOCVtlSLvys27ZwpxG4plel253EBno6WoH7ShdMU4bD1JGebcjr6n-GMB1SNevAVzmg2VIa38ZaFG1lYDq4nGv5dx4zxToUW0_NNgoOTxtbyPZKd9JU3Wyrcpjiunjkd3-PNGhy5-6U02dX1WBwoKwHg3tqpmDJHjuz2cg-q_c=" #telethon string session of user or bot get it from https://replit.com/@MISSKRISTY/MISS-KRISTY
    MONGO_DB_URI = "mongodb+srv://King098:king098@cluster0.lhmvji8.mongodb.net/?retryWrites=true&w=majority" #get it from mongodb.com get
    ARQ_API_KEY = "ZYXASV-RNRLIS-AKGBNQ-NIPHTK-ARQ" #git it form @ARQRobot
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    SQLALCHEMY_DATABASE_URL = "postgres://mcclbjwx:CqMrbec47cqL5KbaZOUDlVQWOscjNcKR@peanut.db.elephantsql.com/mcclbjwx"  # needed for any database modules get it from https://www.elephantsql.com/
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@WizkhalifaSupport"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = [1820525265]
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [1820525265]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = [5323266323]
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = [5323266323]
    WOLVES = [5323266323]
    START_IMG = "https://telegra.ph/file/8fc05e1bc37effdf4302b.jpg" #yor fav img link
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    REM_BG_API_KEY = "uwu"
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = None  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
