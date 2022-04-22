import asyncio

import aiogram
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, db, bot
from states.data import NewPost

@dp.message_handler(text="/sanash", user_id=732585677)
async def send_ad_to_all(message: types.Message):

    count = await db.count_users()

    msg = f"Foydalanuvchilar: {count}"
    await message.answer(msg)

@dp.message_handler(text="/post", user_id = 732585677)
async def create_post(message: types.Message):
    await message.answer("Chop etish uchun post yuboring.", reply_markup=ReplyKeyboardRemove())
    await NewPost.Confirm.set()

@dp.message_handler(state=NewPost.Confirm, content_types=types.ContentTypes.TEXT)
async def enter_message(message: types.Message, state: FSMContext):

    global data
    data={"tekst" : message.parse_entities(as_html=True),
                             "type": "text"}

    await message.answer(message.parse_entities(as_html=True))
    await message.answer(f"Barcha Foydalanuvchilarga Yuborishni Tasdiqlaysizmi?", reply_markup=confirmation_keyboard)
    await NewPost.Send.set()

@dp.message_handler(state=NewPost.Confirm, content_types=types.ContentTypes.PHOTO)
async def enter_message(message: types.Message, state: FSMContext):
    global data
    data = {"foto": message.photo[-1].file_id,
                             "caption": message.parse_entities ( as_html = True ),
                             "type": "photo",
                             "tekst": None}

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=message.photo[-1].file_id,
        caption=message.parse_entities( as_html = True )
        )

    await message.answer(f"Barcha Foydalanuvchilarga Yuborishni Tasdiqlaysizmi?", reply_markup=confirmation_keyboard)

    await NewPost.Send.set()

@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS, state=NewPost.Send)
async def approve_post(call: CallbackQuery, state: FSMContext):
    await call.answer("Chop etishga ruxsat berdingiz", show_alert=True)
    await call.message.edit_reply_markup()
    users = await db.select_all_users()
    count = 0

    for user in users:

        try:
            if data["type"]=="photo":
                await bot.send_photo(chat_id=user[3],photo=data["foto"],caption=data["caption"] )

            elif data["type"]=="text":
                await bot.send_message(chat_id=user[3], text=data["tekst"], parse_mode="HTML")
            count += 1

        except:
            await db.delete_user(user[3])
            await call.message.answer(f"{user[1]} bazadan o'chirildi!")

        await asyncio.sleep(0.05)

    await call.message.answer(f"Barchaga yuborildi: {count}")
    await state.reset_state(with_data=False)

@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS, state=NewPost.Send)
async def decline_post(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.answer("Post rad etildi.", reply_markup=ReplyKeyboardRemove())
    await state.finish()
