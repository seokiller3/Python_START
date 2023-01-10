import api
from tok import token

url = "https://api.telegram.org/"


def start():
    bot = api.MyTelBot(token)
    bot.run_bot()
