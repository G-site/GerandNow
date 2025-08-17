import asyncio
# import logging
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


from app.handlers import router
from app.admin import admin_router
from app.database import data_create
from bot_instance import bot, dp
from app.video import video_loop, video_create


# async def set_bot_name():
    # await bot.set_my_name(name="GerandNow")


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Меню"),
        BotCommand(command="about", description="О нас")
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def set_bot_description(bot: Bot):
    await bot.set_my_short_description("🎬 Получай уведомления о новых видео и шортсах на канале Геранд мгновенно!")
    await bot.set_my_description("🎬 Следите за новыми видео и шортсами на канале Геранд!\nНаш бот мгновенно уведомляет вас о свежих выпусках, показывает красивое превью и описание каждого видео.\n🔔 Будьте всегда в курсе самых новых анимаций и коротких видео!\n\n\n💡 Дополнительно:\nПодписка на уведомления о видео\nБыстрый доступ к сообществу и поддержке\nВозможность поддержать проект звёздами ⭐️")


async def main():
    await data_create()
    await video_create()
    asyncio.create_task(video_loop())
    await set_bot_commands(bot)
    await set_bot_description(bot)
    dp.include_router(router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
