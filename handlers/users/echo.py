import asyncpg
from aiogram import types
from kitobcha_v2 import yakun, get_send
from keyboards.inline.mykb import choice, check_callback
from loader import dp, db

@dp.message_handler()
async def sendnum(message: types.Message):
    await db.create_table_users()
    try:
        await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        await db.update_user_fullname(username=message.from_user.full_name,
                                 telegram_id=message.from_user.id
                                 )
    num = message.text.split()
    if len(num)==2 and num[0].isdigit() and num[1].isdigit() and int(num[1])>int(num[0]):
        if int(num[1])-int(num[0]) < 1501:

            await message.answer("Chop etish shaklini tanlang: ", reply_markup=await choice(f"{num[0]}-{num[1]}"))


        else:
            await message.answer('Betlar soni 1500 dan oshmasligi lozim!')

    elif len(num)==1 and num[0].isdigit():
        await message.answer("Chop etish shaklini tanlang: ", reply_markup=await choice(num[0]))
#


    else:
        await message.answer("Namunadagidek kiriting!")     


@dp.callback_query_handler(check_callback.filter(get='check'))
async def bool(call: types.CallbackQuery, callback_data: dict):

    await call.message.edit_text(f"''{callback_data['approved'].title()}'' rejimi...")
    num = callback_data["num"].split("-")

    if callback_data["approved"] == "kitobcha":
        if len(num) == 2:
            result = yakun(int(num[1]), int(num[0]))

        elif len(num) == 1:
            result = yakun(int(num[0]))
        await call.message.answer(f"Printerga {result['listlar']} ta list joylang! ")
        await call.message.answer(f"<code>{result['qator1'][1:]}</code>")
        await call.message.answer(f"<code>{result['qator2'][1:]}</code>")
    else:
        if len(num) == 2:

            result = get_send(int(num[1]), int(num[0]))

        elif len(num) == 1:
            result = get_send(int(num[0]))

        await call.message.answer(f"Printerga {result['listlar']} ta list joylang! ")
        await call.message.answer(f"<code>{result['qator1'][1:-1]}</code>")
        await call.message.answer(f"<code>{result['qator2'][1:-1]}</code>")
