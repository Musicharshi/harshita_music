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

STRING_SESSION = getenv(","BQDrRfIAu752luI5VI0LXu4wNmSCWZLLb0xnnRmOwdJgBGAWxsHrjMovqbvTT0zeIk_4v792tGF6E_DVSfxeBtoyhgra72CkCUVRBCMBsi762SjsI3oRa1sqsrslgZ611WSTcPwMnYyVHqBY5qJf1Li4XK9SGyuwh9yGw_b3EMM4lHnHC6Gr2e4HzqRAIsfr5DUBrKiVqxIRabnO7G9exFITCvX7hGrwKaOI_foeYYhpc_m0tj6JGz5Y7J6-h3m_SkbzrU3JMSZmyqyyj2FYgIU_YZ7p6UDFILHHGQz4bURWboexgpgv1gG_981jfQwDBjIM5lzePRZZ6u2FoD2E-V1IPjlA7gAAAAFfhezDAA")

OWNER_USERNAME = getenv(","@MR_HARSH_OP")

SUPPORT_GROUP = getenv(","https://t.me/alone_support")
SUPPORT_CHANNEL = getenv(","https://t.me/alone_support")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5897579715").split()))
aiohttpsession = aiohttp.ClientSession()
