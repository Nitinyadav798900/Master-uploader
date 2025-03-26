import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7876428496:AAEo_yM2FrB71qN_sdL8ASTDiFO5N9-YOMQ")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "12475131"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "719171e38be5a1f500613837b79c536f")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "1714266885").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
