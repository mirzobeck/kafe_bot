from aiogram import types
from keyboards.default.catogory import Shashlik, prod
from loader import dp
from aiogram.dispatcher import FSMContext
from states.st import anketa



@dp.message_handler(text="Shashlik",state=anketa.category)
async def orqa1(message: types.Message, state: FSMContext):
    shash = message.text
    data = await state.get_data()
    
    if 'cart' in data.keys():
        cart = data.get('cart')
        await state.update_data(
            {
                'cart': cart
            }
        )
    else:
        await state.update_data(
            {'cat':shash, 'cart': []},
        )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=Shashlik)
    await anketa.next()



@dp.message_handler(text="Kuskavoy (mol go'shti)",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/8MXjNJG", "Kuskavoy (mol go'shti)\n\nNarxi: 13500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Kuskavoy (qo'y go'shti)",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/vDxXnNX", "Kuskavoy (qo'y go'shti)\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Rulet",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/fCZVKzB", "Rulet\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="2 ichida 1",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/RptdkVH", "2 ichida 1\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Napoleon",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/MGFB6Rn", "Napoleon\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Qiymali kabob",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/9WMk5YR", "Qiymali kabob\n\nNarxi: 12500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()