from loader import dp
from aiogram import types
from keyboards.default.catogory import salat, prod
from aiogram.dispatcher import FSMContext
from states.st import anketa


@dp.message_handler(text='Salatlar', state=anketa.category)
async def salAt(message: types.Message, state: FSMContext):
    shash = message.text
    await state.update_data(
        {'cat':shash}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=salat)
    await anketa.next()



@dp.message_handler(text="Olivye",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/9brLns7", "Olivye\n\nNarxi: 20000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Smak",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/m5jy6w5", "Smak\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Cesar",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/wg8wrbM", "Cesar\n\nNarxi: 20000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Fransuzcha",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/8zfLFqv", "Fransuzcha\n\nNarxi: 21000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Mimoza",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/Mc4S3x2", "Mimoza\n\nNarxi: 24000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Селёдка под шубой",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/87N0mt0", "Селёдка под шубой\n\nNarxi: 24000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()