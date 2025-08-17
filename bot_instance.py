from aiogram import Bot, Dispatcher
# from dotenv import load_dotenv
import os

# load_dotenv()
TOKEN = os.environ.get("TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()
