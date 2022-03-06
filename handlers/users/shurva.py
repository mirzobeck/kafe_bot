from keyboards.default.catogory import prod, shorva
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.st import anketa


@dp.message_handler(text="Sho'rva", state=anketa.category)
async def sh(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=shorva)
    await anketa.next()



@dp.message_handler(text="Mastava", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/m5N1h03", "Mastava\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()


@dp.message_handler(text="Moshxurda", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    await message.answer("Kechirasiz, bu taom vaqtincha sotuvda yuq 🙂",reply_markup=shorva)
    await anketa.product.set()


@dp.message_handler(text="Borsh", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/V96PMps", "Borsh\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()


@dp.message_handler(text="Frikadelkali sho'rva", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/x7RWHgK", "Frikadelkali sho'rva\n\nNarxi: 15000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()


@dp.message_handler(text="Sho'rva(mol go'shti)", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/8XNH8kq", "Sho'rva(mol go'shti)\n\nNarxi: 19000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()


@dp.message_handler(text="Solyanka", state=anketa.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/TgTNsVF", "Solyanka\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()