from cgitb import text
from aiogram import types
from keyboards.default.catogory import menyu, Shashlik, prod, balq
from keyboards.default.asos import asosiy, bl
from aiogram.dispatcher import FSMContext
from loader import dp
from states.st import anketa


@dp.message_handler(text='Menu')
async def menu(message: types.Message):
    await message.answer("Xo'sh, buyurtmaga o'tamizmi, sizni issiq taomlarimiz kutmoqda 👨🏻‍🍳🔥",reply_markup=menyu)
    await anketa.category.set()


@dp.message_handler(text="Bosh Sahifa 🏠", state=anketa.product)
async def mennu(message: types.Message, state: FSMContext):
    await message.answer(f"Buyurtma berishni boshlaymizmi?", reply_markup=asosiy)
    await state.finish()





