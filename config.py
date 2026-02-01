import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OSU_SESSION = os.getenv("OSU_SESSION")
PROXY_URL = os.getenv("PROXY_URL")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env")
if not OSU_SESSION:
    raise ValueError("OSU_SESSION is not set in .env")
if not PROXY_URL:
    raise ValueError("PROXY_URL is not set in .env")
