import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Xush kelibsiz, {message.from_user.full_name}! Iltimos telefon raqamingizni kiriting")
"""    try:
        await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        await db.update_user_fullname(username=message.from_user.full_name,
                                 telegram_id=message.from_user.id
                                 )"""
