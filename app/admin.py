from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.exceptions import TelegramAPIError


from app.database import check_admin, get_users
import app.keyboards as kb


admin_router = Router()


@admin_router.message(Command('admin'))
async def admin(message: Message):
    tg_id = message.from_user.id
    name = message.from_user.first_name
    status = await check_admin(tg_id)

    if status == 'Creator':
        await message.answer(f"Добро пожаловать в админ-панель, <b>{name}</b>!", reply_markup=kb.admin_menu, parse_mode="HTML")
    else:
        await message.answer("Извините, но вы не являетесь Администратором.")


@admin_router.callback_query(F.data == 'download_static')
async def static_download(callback: CallbackQuery):
    try:
        file = FSInputFile('database.db')
        await callback.message.answer_document(file, caption="База данных 📂")
    except Exception as e:
        await callback.message.answer(f"Ошибка при отправке БД: {e}")


@admin_router.callback_query(F.data == 'message3')
async def subscribe(callback: CallbackQuery):
    users = await get_users()
    sent = 0
    for tg_id in users:
        try:
            await callback.bot.send_message(
                chat_id=tg_id,
                text="<b>🔥 Не пропусти важное!</b>\nПодпишись на наш Telegram-канал, чтобы быть в курсе новостей и получать бонусы 🎁",
                parse_mode="HTML",
                reply_markup=kb.subscribe
            )
            sent += 1
        except TelegramAPIError as e:
            print(f"Ошибка, не всем отправлено, {e}")
    await callback.answer(f"✅ Отправлено {sent} пользователям!")


@admin_router.callback_query(F.data == 'message2')
async def share(callback: CallbackQuery):
    users = await get_users()
    sent = 0
    for tg_id in users:
        try:
            await callback.bot.send_message(
                chat_id=tg_id,
                text="<b>🤖 Понравился бот?</b>\n\n<i>Поделись им с другом, чтобы и он мог воспользоваться!</i>\n\n",
                parse_mode="HTML",
                reply_markup=kb.share
            )
            sent += 1
        except TelegramAPIError as e:
            print(f"Ошибка, не всем отправлено, {e}")
    await callback.answer(f"✅ Отправлено {sent} пользователям!")


@admin_router.callback_query(F.data == 'message1')
async def tech(callback: CallbackQuery):
    users = await get_users()
    sent = 0
    for tg_id in users:
        try:
            await callback.bot.send_message(
                chat_id=tg_id,
                text="<b>🔧 Внимание!</b>\nСкоро будет проведено <b>техническое обслуживание</b> сервиса.\nСпасибо за понимание!",
                parse_mode="HTML"
            )
            sent += 1
        except TelegramAPIError as e:
            print(f"Ошибка, не всем отправлено, {e}")
    await callback.answer(f"✅ Отправлено {sent} пользователям!")
