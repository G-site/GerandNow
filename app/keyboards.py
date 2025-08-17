from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='О нас', callback_data='about')]
    # [InlineKeyboardButton(text='Поддержать проект', callback_data='donate')]
    ])


about_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Телеграм-канал', url='https://t.me/gerandnow_news')],
    [InlineKeyboardButton(text='Служба поддержки', url='https://t.me/TanksCK')]])


def watch_menu(link):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Смотреть", url=link)]
    ])


admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Скачать статистику', callback_data='download_static')],
    [InlineKeyboardButton(text='Сообщить о тех-перерыве', callback_data='message1')],
    [InlineKeyboardButton(text='Попросить поделиться с другом', callback_data='message2')],
    [InlineKeyboardButton(text='Попросить подписаться на тгк', callback_data='message3')]])


subscribe = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Подписаться', url='https://t.me/gerandnow_news')]])


share = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Поделиться', switch_inline_query="")]])
