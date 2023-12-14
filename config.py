from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9c6cce0fdd21dfd7e7d06.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e572bb3a7345c4400eced.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https:..")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/..")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/file/bd814b9e5907c4548e7c3.jpg"
