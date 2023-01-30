import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","))

DURATION_LIMIT = int(getenv("DURATION_LIMIT","300"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME",)

OWNER_ID = list(map(int, getenv("OWNER_ID",)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",https://github.com/Musicharshi/musicharshi")

START_IMG_URL = getenv(
    "START_IMG_URL", )

STRING_SESSION = getenv("STRING_SESSION")

OWNER_USERNAME = getenv("OWNER_USERNAME")

SUPPORT_GROUP = getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
