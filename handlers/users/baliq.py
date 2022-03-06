from aiogram import types
from keyboards.default.catogory import prod, balq
from loader import dp
from aiogram.dispatcher import FSMContext
from states.st import anketa



@dp.message_handler(text="Baliq 🐠", state=anketa.category)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
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
            {'cat':cat, 'cart': []},
        )
    
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=balq)
    await anketa.next()



@dp.message_handler(text="Sazan (300g)", state=anketa.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/XYMMF4D", "Sazan (300g)\n\nNarxi: 45000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Sudak (300g)", state=anketa.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo("https://ibb.co/D7m47gs", "Sudak (300g)\n\nNarxi: 48000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Sous 300ml", state=anketa.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Sous 300ml\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()



@dp.message_handler(text="Sous 500ml", state=anketa.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer("Sous 500ml\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=prod)
    await anketa.next()




