from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery


import app.keyboards as kb
from app.database import set_user


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await set_user(message.from_user.id, message.from_user.username,  message.from_user.first_name)
    await message.answer_photo(photo="https://i.ibb.co/fGKVpfj2/16-C1-CD23-C.png", caption="<b>Привет! 👋 Добро пожаловать в бота GerandNow! 🎬</b>\n\n<i>С этого момента ты всегда будешь в курсе всех новых видео, шортс и прямых эфиров. 📹🔥\nБольше не нужно проверять канал вручную — бот пришлёт уведомление сразу, как только выйдет новое видео! 🚀</i>\n\n<b>Что тебя ждёт:</b>\n• Свежие видео и шортс с канала 🎞\n• Уведомления о прямых эфирах и премьерах 📢\n• Краткие описания и ссылки на видео для быстрого просмотра 🔗\n• Возможность всегда быть в центре событий  вселенной Геранд ✨", reply_markup=kb.start_menu, parse_mode="HTML")


@router.message(Command('about'))
async def about(message: Message):
    await message.answer_photo(photo="https://i.ibb.co/MD4mQNNX/16-B4544-D0.png", caption="<b>О нас 🎬</b>\n\nПривет! 👋 Мы – команда, которая создала этого бота специально для фанатов канала Геранд. 📹🔥\n\nНаша цель – сделать так, чтобы ты никогда не пропускал новые видео, шортс и прямые эфиры. \nС этим ботом тебе больше не нужно проверять канал вручную – мы пришлём уведомление сразу, как только выйдет что-то новое! 🚀\n\n<b>Что мы предлагаем:</b>\n• Уведомления о свежих видео и шортс 🎞\n• Ссылки на видео для быстрого просмотра 🔗\n• Оповещения о прямых эфирах и премьерах 📢\n• Лёгкий и удобный способ быть в курсе всего происходящего на канале Геранд ✨\n\nНе забудь <b>вступить в наш Telegram-канал</b>, чтобы быть в курсе всех новостей, участвовать в обсуждениях и не пропускать эксклюзивный контент! 💬", reply_markup=kb.about_menu, parse_mode="HTML")


@router.callback_query(F.data == 'about')
async def about2(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://i.ibb.co/MD4mQNNX/16-B4544-D0.png", caption="<b>О нас 🎬</b>\n\nПривет! 👋 Мы – команда, которая создала этого бота специально для фанатов канала Геранд. 📹🔥\n\nНаша цель – сделать так, чтобы ты никогда не пропускал новые видео, шортс и прямые эфиры. \nС этим ботом тебе больше не нужно проверять канал вручную – мы пришлём уведомление сразу, как только выйдет что-то новое! 🚀\n\n<b>Что мы предлагаем:</b>\n• Уведомления о свежих видео и шортс 🎞\n• Ссылки на видео для быстрого просмотра 🔗\n• Оповещения о прямых эфирах и премьерах 📢\n• Лёгкий и удобный способ быть в курсе всего происходящего на канале Геранд ✨\n\nНе забудь <b>вступить в наш Telegram-канал</b>, чтобы быть в курсе всех новостей, участвовать в обсуждениях и не пропускать эксклюзивный контент! 💬", reply_markup=kb.about_menu, parse_mode="HTML")
