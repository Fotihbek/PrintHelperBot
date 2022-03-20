from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}, hujjat faylining sahifalari sonini kiriting!\nTo'liq ma'lumot /yordam buyrug'ini yuboring.")
