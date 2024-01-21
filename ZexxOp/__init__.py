from ZexxOp.core.bot import ZexxOpBot
from ZexxOp.core.dir import dirr
from ZexxOp.core.git import git
from ZexxOp.core.userbot import Userbot
from ZexxOp.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = ZexxOpBot()

userbot = Userbot(Client)


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
