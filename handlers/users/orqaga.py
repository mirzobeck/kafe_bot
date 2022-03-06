from states.st import anketa
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from keyboards.default.catogory import menyu, Shashlik, balq, zaquska, salat, water, shorva
from keyboards.default.asos import asosiy


@dp.message_handler(text="ORQAGA ↩️", state=anketa.savat0)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", reply_markup=asosiy)
    await state.finish()


@dp.message_handler(text="ORQAGA ↩️",state=anketa.savat)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer("Davom etamizmi? 👨🏻‍🍳🔥",reply_markup=menyu)
    await anketa.category.set()


@dp.message_handler(text="ORQAGA ↩️", state=anketa.savat2)
async def orqa1(message: types.Message, state: FSMContext):
    # await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", reply_markup=menyu)
    data = await state.get_data()
    cat = data.get('cat')
    if cat == 'Shashlik':
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", reply_markup=Shashlik)
        await anketa.product.set()
    elif cat == 'Baliq 🐠':
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=balq)
        await anketa.product.set()
    elif cat == 'Холодные закуски':
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=zaquska)
        await anketa.product.set()
    elif cat == "Salatlar":
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=salat)
        await anketa.product.set()
    elif cat == "Ichimliklar 🥤":
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=water)
        await anketa.product.set()
    elif cat == "Sho'rva":
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=shorva)
        await anketa.product.set()



@dp.message_handler(text="ORQAGA ↩️",state=anketa.category)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer(f"Sahifani tanlang 😊", reply_markup=asosiy)
    await state.finish()


@dp.message_handler(text="ORQAGA ↩️",state=anketa.product)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer("Xo'sh, buyurtmaga o'tamizmi, sizni issiq taomlarimiz kutmoqda 👨🏻‍🍳🔥",reply_markup=menyu)
    await anketa.category.set()




@dp.message_handler(text="ORQAGA ↩️",state=anketa.amout)
async def orqa1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    cat = data.get('cat')
    if cat == 'Shashlik':
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", reply_markup=Shashlik)
        await anketa.product.set()
    elif cat == 'Baliq 🐠':
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=balq)
        await anketa.product.set()
    elif cat == 'Холодные закуски':
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=zaquska)
        await anketa.product.set() 
    elif cat == "Salatlar":
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=salat)
        await anketa.product.set() 
    elif cat == "Ichimliklar 🥤":
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=water)
        await anketa.product.set() 
    elif cat == "Sho'rva":
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=shorva)
        await anketa.product.set()
    