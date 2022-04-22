from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

savekb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard = [
    [
        KeyboardButton(text="📨 Saqlash")
    ]
])



cancelkb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard = [
    [
        KeyboardButton(text="❌ Bekor qilish")
    ]
])
