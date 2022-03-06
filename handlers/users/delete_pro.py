from aiogram.types import ReplyKeyboardMarkup
from loader import dp, db
from aiogram import types
from handlers.users.narxi import get_price, price
from states.st import anketa
from keyboards.default.catogory import menyu, Shashlik, balq, zaquska, salat, water, shorva
from aiogram.dispatcher.storage import FSMContext
from keyboards.default.asos import asosiy



@dp.message_handler(text_contains="❌", state=anketa.savat0)
async def delete_product(message: types.Message, state: FSMContext):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Buyurtma berish 🚚")
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Savatcham:\n\n"
    nb = 1
    if len(products) == 0:
        await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", reply_markup=asosiy)
        await state.finish()
    else:
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            pricee = get_price(product[1], product[2])
            total += pricee
            msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
            nb += 1

            msg += f"\nJami: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)


@dp.message_handler(text="Bo'shatish 🗑", state=anketa.savat0)
async def clearcart(message: types.Message, state: FSMContext):
    id = message.from_user.id
    db.clear_cart(tg_id=id)

    await message.answer("Davom etamizmi? 👨🏻‍🍳🔥", reply_markup=asosiy)
    await state.finish()







@dp.message_handler(text_contains="❌", state=anketa.savat)
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Buyurtma berish 🚚")
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Savatcham:\n\n"
    nb = 1
    if len(products) == 0:
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", reply_markup=menyu)
        await anketa.category.set()
    else:
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            pricee = get_price(product[1], product[2])
            total += pricee    
            msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
            nb += 1

            msg += f"\nJami: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)


@dp.message_handler(text="Bo'shatish 🗑", state=anketa.savat)
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", reply_markup=menyu)
    await anketa.category.set()







@dp.message_handler(text_contains="❌", state=anketa.savat2)
async def delete_product(message: types.Message, state: FSMContext):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Buyurtma berish 🚚")
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Savatcham:\n\n"
    nb = 1
    if len(products) == 0:
        data = await state.get_data()
        cat = data.get('cat')
        if cat == 'Shashlik':
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", reply_markup=Shashlik)
            await anketa.product.set()
        elif cat == 'Baliq 🐠':
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=balq)
            await anketa.product.set()
        elif cat == 'Холодные закуски':
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=zaquska)
            await anketa.product.set()
        elif cat == "Salatlar":
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=salat)
            await anketa.product.set()
        elif cat == "Ichimliklar 🥤":
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=water)
            await anketa.product.set()
        elif cat == "Sho'rva":
            await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=shorva)
            await anketa.product.set()
    else:
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            pricee = get_price(product[1], product[2])
            total += pricee
            msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
            nb += 1

            msg += f"\nJami: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)


@dp.message_handler(text="Bo'shatish 🗑", state=anketa.savat2)
async def clearcart(message: types.Message, state: FSMContext):
    id = message.from_user.id
    db.clear_cart(tg_id=id)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    data = await state.get_data()
    cat = data.get('cat')
    if cat == 'Shashlik':
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", reply_markup=Shashlik)
        await anketa.product.set()
    elif cat == 'Baliq 🐠':
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=balq)
        await anketa.product.set()
    elif cat == 'Холодные закуски':
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=zaquska)
        await anketa.product.set()
    elif cat == "Salatlar":
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=salat)
        await anketa.product.set()
    elif cat == "Ichimliklar 🥤":
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=water)
        await anketa.product.set()
    elif cat == "Sho'rva":
        await message.answer("Savatchangiz bo'shatildi.\n\nDavom etamizmi? 👨🏻‍🍳🔥", parse_mode='html', reply_markup=shorva)
        await anketa.product.set()
