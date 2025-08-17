from googleapiclient.discovery import build
import asyncio
import aiosqlite
import os
# from dotenv import load_dotenv


from bot_instance import bot
import app.keyboards as kb
from app.database import get_users


CHANNEL_ID = "UCSYOvRiB12CnApfSC_GeFXg"
DB_PATH = "video.db"


# load_dotenv()
YOUTUBE_API_KEYS = [os.environ.get(f"YOUTUBE_API_KEY{i}") for i in range(1, 21) if os.environ.get(f"YOUTUBE_API_KEY{i}")]
current_key_index = 0


async def video_create():
    async with aiosqlite.connect(DB_PATH) as db:
        query = """
            CREATE TABLE IF NOT EXISTS video(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_id VARCHAR
            )
        """
        await db.execute(query)
        await db.commit()


def get_youtube_client():
    global current_key_index
    key = YOUTUBE_API_KEYS[current_key_index]
    current_key_index = (current_key_index + 1) % len(YOUTUBE_API_KEYS)
    return build("youtube", "v3", developerKey=key)


async def get_last_video_id():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT video_id FROM video ORDER BY id DESC LIMIT 1")
        row = await cursor.fetchone()
        return row[0] if row else None


async def save_video_id(video_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO video (video_id) VALUES (?)", (video_id,))
        await db.commit()


def get_latest_video():
    youtube = get_youtube_client()
    response = youtube.search().list(
        part="id,snippet",
        channelId=CHANNEL_ID,
        order="date",
        maxResults=1
    ).execute()

    if not response.get("items"):
        return None, None, None, None

    item = response["items"][0]
    video_id = item["id"].get("videoId")
    title = item["snippet"]["title"]
    thumbnail = item["snippet"]["thumbnails"]["high"]["url"]
    url = f"https://www.youtube.com/watch?v={video_id}"

    return video_id, title, thumbnail, url


async def check_youtube():
    video_id, title, thumbnail, url = get_latest_video()
    if not video_id:
        return None

    last_video_id = await get_last_video_id()
    if last_video_id != video_id:
        await save_video_id(video_id)
        print(f"[DB] Добавлено новое видео: {video_id}")
        return title, url, thumbnail
    return None


async def notify_users(title, url, thumbnail):
    users = await get_users()
    for tg_id in users:
        try:
            await bot.send_photo(
                chat_id=tg_id,
                photo=thumbnail,
                caption=f"🎬<b>{title}</b>\n\n🎥Новое видео уже на канале Gerand!",
                parse_mode="HTML",
                reply_markup=kb.watch_menu(url)
            )
        except Exception as e:
            print(f"Не удалось отправить {tg_id}: {e}")


async def video_loop():
    await video_create()
    while True:
        result = await check_youtube()
        if result:
            title, url, thumbnail = result
            await notify_users(title, url, thumbnail)
        await asyncio.sleep(60)
