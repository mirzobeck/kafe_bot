from loader import dp
from aiogram import types
from keyboards.default.catogory import zaquska
from states.st import anketa
from aiogram.dispatcher import FSMContext
from keyboards.default.catogory import prod

@dp.message_handler(text="Холодные закуски", state=anketa.category)
async def v(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=zaquska)
    await anketa.next()



@dp.message_handler(text='Suzma',state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/txBwFCS", "Suzma\n\nNarxi: 7500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Ruscha Seld balig'i",state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/56NbjCj", "Ruscha Seld balig'i\n\nNarxi: 21000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text='Assorti',state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/xHfXcHX", "Assorti\n\nNarxi: 72000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text='Xolodes',state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/6w6C8Yd", "Xolodes\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text='Assorti (tuzli)',state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/z5Pp4wk", "Assorti (tuzli)\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text='Свежие нарезки',state=anketa.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/5rGbdxk", "Свежие нарезки\n\nNarxi: 15000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()