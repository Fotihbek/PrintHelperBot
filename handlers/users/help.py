from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands=["yordam"])
async def bot_help(message: types.Message):
    text = ("Hujjatni, birinchi sahifasidan boshlab chop etmoqchi bo'lsangiz, shunchaki, necha bet ekanini yoki nechinchi betgacha chiqarmoqchi ekaningizni kiriting. Agar, hujjatning birinchi betidan emas, orasidan boshlashni ixtiyor qilsangiz, <b>55 100</b> shaklida yuboring! Bunda, ``55-betdan, 100-betgacha chop etish buyrug'i berilgan`` deb qaraladi.\n👨‍💻 Dasturchi: Komilov Fotihbek")
    
    await message.answer(text)
