import os

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
MONGO_URI = os.getenv("MONGO_URI")
SESSION = os.getenv("SESSION")
PREFIX = os.getenv("PREFIX", "*")
PRIME_LOGO = os.getenv(
    "PRIME_LOGO",
    "https://telegra.ph/file/7e0c2450664bfc304203b.jpg")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
HEROKU_API = os.getenv("HEROKU_API", None)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
REPO_URL = os.getenv("REPO_URL", "https://github.com/Toni880/Prime-Userbot")