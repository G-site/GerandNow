from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import LabeledPrice
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery


from bot_instance import bot


donate_router = Router()


@donate_router.message(Command('donate'))
async def donate(message: Message):
    prices = [
        LabeledPrice(label="5 ⭐", amount=5*100),
        LabeledPrice(label="10 ⭐", amount=10*100),
        LabeledPrice(label="20 ⭐", amount=20*100),
        LabeledPrice(label="50 ⭐", amount=50*100),
        LabeledPrice(label="100 ⭐", amount=100*100),
        LabeledPrice(label="200 ⭐", amount=200*100),
        LabeledPrice(label="500 ⭐", amount=500*100)
    ]
    await message.answer_invoice(title="💖 Поддержи проект!", description="Каждое ваше пожертвование помогает нам развивать бота и добавлять новые функции.\nВы можете поддержать проект малой суммой — всего несколько звёзд ⭐, или выбрать любую удобную вам сумму.\n\nНажмите на кнопку ниже, чтобы сделать пожертвование:", payload="donate_payload", currency="STARS", start_parameter="donate", prices=prices)


@donate_router.callback_query(F.data == 'donate')
async def donate2(callback: CallbackQuery):
    prices = [
        LabeledPrice(label="5 ⭐", amount=5*100),
        LabeledPrice(label="10 ⭐", amount=10*100),
        LabeledPrice(label="20 ⭐", amount=20*100),
        LabeledPrice(label="50 ⭐", amount=50*100),
        LabeledPrice(label="100 ⭐", amount=100*100),
        LabeledPrice(label="200 ⭐", amount=200*100),
        LabeledPrice(label="500 ⭐", amount=500*100)
    ]
    await callback.message.answer_invoice(title="💖 Поддержи проект!", description="Каждое ваше пожертвование помогает нам развивать бота и добавлять новые функции.\nВы можете поддержать проект малой суммой — всего несколько звёзд ⭐, или выбрать любую удобную вам сумму.\n\nНажмите на кнопку ниже, чтобы сделать пожертвование:", payload="donate_payload", currency="STARS", start_parameter="donate", prices=prices)


@donate_router.pre_checkout_query()
async def process_pre_checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@donate_router.message(F.successful_payment)
async def process_payment(message: Message):
    await message.answer_photo(photo="https://i.ibb.co/fGKVpfj2/16-C1-CD23-C.png", caption="<b>💖 Спасибо!</b>\nВаше пожертвование очень важно для нас.\nБлагодаря вам проект продолжает жить и развиваться. 🙏", message_effect_id=1)