import logging
from kitobcha_v2 import yakun

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2068238787:AAHv0yfEVcDcNJ4Rd4K3_tS2-YuJQRGx0p0'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("""Bot yordamida kitob chop etish haqida yo'riqnoma bilan /help buyrug'i orqali tanishishingiz mumkin. 
📖 Necha betli kitob chiqarmoqchisiz?""")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    
    await message.reply("Kitobcha chiqarish yo'riqnomasi: https://telegra.ph/Printer-orqali-kitobcha-chiqarish-texnikasi-09-29 ")

@dp.message_handler(commands=['coder'])
async def send_help(message: types.Message):
    
    await message.reply("Dasturchi: Fotihbek Komilov \nMurojaat: @ProgerUzb")



@dp.message_handler()
async def sendnum(message: types.Message):
    

    num = message.text.split()
    
    if len(num)==2 and num[0].isdigit() and num[1].isdigit() and int(num[1])>int(num[0]):
        if int(num[1])-int(num[0]) < 1501:

            result = yakun(int(num[1]), int(num[0]))
            await message.answer(f"Printerga {result['listlar']} ta list joylang! ")
            await message.answer(result['qator1'][1:])
            await message.answer(result['qator2'][1:])

        
        else:
            await message.answer('Betlar soni 1500 dan oshmasligi lozim!')

    elif len(num)==1 and num[0].isdigit():
        result = yakun(int(num[0]))
        await message.answer(f"Printerga {result['listlar']} ta list joylang! ")
        await message.answer(result['qator1'][1:])
        await message.answer(result['qator2'][1:])

    else:
        await message.answer("Namunadagidek kiriting!")     

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
