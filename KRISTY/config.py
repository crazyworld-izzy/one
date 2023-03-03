import json
import os


def get_user_list(config, key):
    with open("{}/KRISTY/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
     
    API_ID = 22766050  # integer value, dont use "" this sign get it form my.telegram.org
    API_HASH = "092af0023f22b00248071887b1a74efa" # get it form my.telegram.org
    TOKEN = "6233388086:AAEO8W5qNRSMaOHxhBkNEpMHv5KfTu-xSOg"  # get it form @botfather.
    OWNER_ID = 6021591808  # got to @miss_kristy_bot and type /id
    OWNER_USERNAME = "Pacha_pulla_nannu" # your telegram username
    ALLOW_CHATS = True # leave it as it is
    BOT_USERNAME = "One_love_management_bot" # your bot username get it form @botfather
    SUPPORT_CHAT = "https://t.me/one_love_management"  # Your own group for support, do not add the @ if you dont have leave it as it is
    UPDATES_CHANNEL = "https://t.me/one_love_management"  # Your own chsnnel for support, do not add the @ if you dont have leave it as it is
    JOIN_LOGGER =  (
        -1001523625722
    )  # add @miss_kristy_bot in your group and type /id
    EVENT_LOGS = (
        -1001523625722
    )  # add @miss_kristy_bot in your group and type /id
    ERROR_LOG = (
        -1001523625722
    )  # add @miss_kristy_bot in your group and type /id
    STRICT_GMUTE = True #to allow gmutes
    START_STICKER = "" #sticker id for start animation
    TEMP_DOWNLOAD_DIRECTORY = ". /" # dont change
    OPENWEATHERMAP_ID = None



    # RECOMMENDED
    STRING_SESSION ="BQCZ368I97g6dpzYniJ59EmSjXEHmD9ewtuj0ZRHDqgEzDqoFMLUIcRQNFXmNDTUKn7k7N2K4e8X1OlJTFOS943tPxAV_eKfTL_w_9uKodsZn-p9p6Oy594QNIUaRk3G8jPSY6bfGyDDin9HdkMq6IbiKSa1Xcd6ilU0HhhkZ-XdDyyD6BTIkJpKvpamgGCw65Ycf8qu5ICeKpBY5VkeeUXDl-8Dbo-wVbtBCfaaYoW6z3Jrqm-yux86O41Dle_Gy4AejhQortZ_bD193q6_ox9E0JbdoFRmaJaQLYTpmaiHlx7OEIy_fKGEuIkQn3Bgr0gubJTue4prNPFu9kTldK0LAAAAAV-qRMkA" #telethon string session of user or bot get it from https://replit.com/@MISSKRISTY/MISS-KRISTY
    MONGO_DB_URI = "mongodb+srv://King098:king098@cluster0.lhmvji8.mongodb.net/?retryWrites=true&w=majority" #get it from mongodb.com get
    ARQ_API_KEY = "ZYXASV-RNRLIS-AKGBNQ-NIPHTK-ARQ" #git it form @ARQRobot
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    SQLALCHEMY_DATABASE_URL = "postgres://adkdmsyl:36pn6bpyGsXdXR1uxGWCLuGma_S55Zbs@snuffleupagus.db.elephantsql.com/adkdmsyl"  # needed for any database modules get it from https://www.elephantsql.com/
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "https://t.me/one_love_management"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = [6021591808]
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [6021591808]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = [6021591808]
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = [6021591808]
    WOLVES = [6021591808]
    START_IMG = "https://te.legra.ph/file/1e5a7fa65456e3fa7d54d.jpg" #yor fav img link
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
