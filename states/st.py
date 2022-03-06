from aiogram.dispatcher.filters.state import StatesGroup, State


class anketa(StatesGroup):
    category = State()
    product = State()
    amout = State()
    savat0 = State()
    savat = State()
    savat2 = State()