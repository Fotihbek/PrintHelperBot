from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    Confirm = State()
    Send = State()
