## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAAMNteGrECz56LXDn2At1LAXEdsze_T16URkoFJc5swlshWLgqyG9mzUDZ6cZpi8lg7WoD2RbAqX9gpV2HoWHdHIc0Y3aI7NXmLRDQFloWTFxz-iD5DtDo1yJyWX9-n59cg8M_hXKPxDMdMG2n70dCKsS5MdyYH8-qa2gejvC-IbPLjBT80dq-Gt_E_2QthBprNR09NkdSWTfvKklqFEqqa8v8HQcOuzQKcahPDNbtXcgvHuccntMdUc5NvpXIbvfdFeKJV8-Gg8elwBfQZ0An5bxy4njKh54wLh7BCMXWf1QgwAXYFnj9cfWetjrBk0l-rupwUtwH9YZVKD7__u0JAAAAAT_gq8AA")
BOT_TOKEN = getenv("BOT_TOKEN", "5536017329:AAE50QV89YPmMLevNaxZ2mSXfpDKVTK_-7A")
BOT_NAME = getenv("BOT_NAME", "𝐀𝐩𝐩𝐥𝐞 𝐗 𝐌𝐮𝐬𝐢𝐜 🇮🇳")
API_ID = int(getenv("API_ID", "14447155"))
API_HASH = getenv("API_HASH", "ef370b85866716be28c348f5f96db1e4")
OWNER_NAME = getenv("OWNER_NAME", "[ 🇮🇳 ] 𝗧.𝗬 𝗢𝗪𝗡𝗘𝗥")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Am_TrickyYash")
ALIVE_NAME = getenv("ALIVE_NAME", "[ 🇮🇳 ] 𝗧.𝗬 𝗢𝗪𝗡𝗘𝗥")
BOT_USERNAME = getenv("BOT_USERNAME", "AppleXMusic_Bot")
OWNER_ID = getenv("OWNER_ID", "5442143084")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AppleXMusicAssistant_Bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TeamTrickyYash")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TrickyYash")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5485497872 5366655936 5442143084").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c9f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
