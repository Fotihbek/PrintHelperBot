from aiogram import types
from kitobcha_v2 import yakun

from loader import dp


# Echo bot
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

