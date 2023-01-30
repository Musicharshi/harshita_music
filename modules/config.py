import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID","15418866"))

API_HASH = getenv("API_HASH","dbbf679a4b429fab1bfea0b52b8f9be8")

BOT_TOKEN = getenv("BOT_TOKEN", "5850385258:AAGgtswykyvc9OO9i1hHlECPRMmTvtBruDI")

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://vcbot:vcbot@cluster0.yqipgxg.mongodb.net/?retryWrites=true&w=majority")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001618068091"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT","300"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","harsh")

OWNER_ID = list(map(int, getenv("OWNER_ID","5897579715")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO","https://github.com/Musicharshi/musicharshi")

START_IMG_URL = getenv(
    "START_IMG_URL", )

STRING_SESSION = getenv(", "BQDrRfIARx85ukDWlKmt73lk8UuscJTUrvXbqW87ZmunknWb5n9kUZGp78bucM2aRLXwyWOfEFxWSKqeAR73ndYJ5Br5W1Jq6-B3a6Pl-nRJsvf_salGzQPa0RN8RE_WytasKnMtUf8ECCpUcAMwfouy15i_ey4k_NNlMp7t3T05xvDj1mWPTnS9ZrP5p9FAfa2oIb1km1RFE7IIr8bXXyqyEaAyuGYyvCBqtvhnuNiqK9btGQSvgYius6h-JCGC5Xi-FP1Qm1COqrwoUTRiKWZSScINAKBz917ViZYdjJAman23AlPncb_rRzbARMFSaFYlNbhXO24uXAIWtgT8PNvQX_72pQAAAAFfhezDAA")

OWNER_USERNAME = getenv(","@MR_HARSH_OP")

SUPPORT_GROUP = getenv(","https://t.me/alone_support")
SUPPORT_CHANNEL = getenv(","https://t.me/alone_support")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5897579715").split()))
aiohttpsession = aiohttp.ClientSession()
