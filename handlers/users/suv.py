from loader import dp
from aiogram import types
from keyboards.default.catogory import water,prod
from aiogram.dispatcher import FSMContext
from states.st import anketa


@dp.message_handler(text="Ichimliklar 🥤", state=anketa.category)
async def wat(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=water)
    await anketa.next()


@dp.message_handler(text="Coca-Cola (0,5 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Coca-Cola (0,5 L)\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Coca-Cola (1,0 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Coca-Cola (1,0 L)\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Coca-Cola (1,5 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Coca-Cola (1,5 L)\n\nNarxi: 13000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Fanta (0,5 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Fanta (0,5 L)\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Fanta (1,0 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Fanta (1,0 L)\n\nNarxi: 10000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Fanta (1,5 L)", state=anketa.product)
async def yarim(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Fanta (1,5 L)\n\nNarxi: 13000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()