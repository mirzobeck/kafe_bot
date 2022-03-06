from aiogram import types
from keyboards.default.asos import bl
from aiogram.dispatcher.storage import FSMContext
from states.st import anketa
from loader import dp


@dp.message_handler(text='Buyurtma berish 🚚', state=anketa.savat0)
async def by(message: types.Message, state: FSMContext):
    await message.answer('Hozircha buyurtma berolmaysiz! ❌')





