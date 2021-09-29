import logging
from funksiya import yakun

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2030202366:AAFxP3UqAuDdY9r3zfGXXcbMi_SjKzHX4tI'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("""Printer orqali kitoblar chop etishda ko'mak beruvchi botga xush kelibsiz! Bot yordamida kitob chop etish haqida yo'riqnoma bilan /help buyrug'i orqali tanishishingiz mumkin. 
📖 Necha betli kitob chiqarmoqchisiz?""")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    
    await message.reply("Kitobcha chiqarish yo'riqnomasi: https://telegra.ph/Printer-orqali-kitobcha-chiqarish-texnikasi-09-29 ")



@dp.message_handler()
async def sendnum(message: types.Message):
    
    try:
        result = yakun(message.text)
        await message.answer(f"Printerga {result['listlar']} ta list joylang! ")
        await message.answer(result['qator1'][1:])
        await message.answer(result['qator2'][1:])

    except:
        await message.answer('Iltimos, son kiriting!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
