from os import environ 

class Config:
    API_ID = environ.get("API_ID", "934337")
    API_HASH = environ.get("API_HASH", "7e55bf98380e16d5de1c4c567395a32")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6805368362:AASfFKFWIDQmcEWlxpFzvchmdZrwI3aoQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://@cluster0.pxk4s9x.mongodb.net/?retryWrites=true&w=majority
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6040965491').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
