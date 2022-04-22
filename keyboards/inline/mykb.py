from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

check_callback = CallbackData('def', 'approved', 'get', "num")

async def choice(son):
    checkkb = InlineKeyboardMarkup(row_width=2)
    checkkb.add(InlineKeyboardButton(text="Kitobcha", callback_data=check_callback.new(approved="kitobcha", get="check", num=son )))
    checkkb.insert(InlineKeyboardButton(text="Hujjat fayli", callback_data=check_callback.new(approved="hujjat fayli", get="check", num=son)))
    return checkkb
