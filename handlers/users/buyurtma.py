from aiogram import types
from keyboards.default.asos import bl
from aiogram.dispatcher.storage import FSMContext
from states.st import anketa
from loader import dp


@dp.message_handler(text='Buyurtma berish 🚚', state=anketa.savat0)
async def by(message: types.Message, state: FSMContext):
    await message.answer('Buyurtma turini tanlang', reply_markup=bl)


@dp.message_handler(text='Bekor qilish♨️', state=anketa.savat0)
async def ba(message: types.Message, state: FSMContext):
    await message.answer('Buyurtma berish fikringizdan qaytganingizdan afsusdamiz😞', reply_markup=asosiy)
    await state.finish()



