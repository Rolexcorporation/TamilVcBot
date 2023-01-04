from os import environ
# import logging
from pyrogram import Client, idle

API_ID = int(environ["26885114"])
API_HASH = environ["41bb6d1f706da3bfbe95a820f427ae78"]
SESSION_NAME = environ["5832249400:AAHz02Tf31BGOsXT7O6i-6PoEP1eUTPPdts"]

plugins = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED by @madanopcon')
idle()
app.stop()
print('\n>>> USERBOT STOPPED by @madanopcon')

