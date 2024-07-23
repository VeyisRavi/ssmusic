import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25953384"))
API_HASH = getenv("API_HASH", "133f1bedccdc3510d8fa5d44e460eab3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7491068145:AAGgtoQ_BrcRgHzmBlkNm2BirMi_m9cqubY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://abbaslinatiq58:natiq.3169@cluster0.2w9vfhx.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002057111740"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7127602239"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-21104551-5c99-4bde-b72d-2f3b1aa5f50c")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Abbasov04/ssmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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")  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TuraResmi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TuraSupportt")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgFHDoIAgBjejeckYIg5dAyeG_MmD2jdZqj1dXC01WevRguPTLB6D0qNAsJ9kxqgFTQmNDda2HtNIrqutyA0UQgG1HbaWM5A0IMxV1c9GBAtRN54OTLS2dOEgzuQXz9qt88pacdOA8s0xOvTBxawjdH5N7Yi6jUF9mgRVF18OTqESVZNWT4d4yxcLSeavotiEWVzBUdfSZLCiBxd0l7U8RDWjNTkWMR4f1o8cADwhsG9x6JenqNXvBPJ9hJ1kBy9laXtiw60ZF60uREO67B6qSiaRElN1V3GAq9KG-S2pqmZVwTyLs0At7VbpdiMrYHPnlmJkRTuop7_ZOK_8_iHb2Ye4ObIygAAAAGYinxeAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/90d5dbb28269820702283.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
STATS_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/857b6d0b04b06017952fa.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
