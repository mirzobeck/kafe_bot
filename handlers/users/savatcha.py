from loader import dp, db
from aiogram import types
from states.st import anketa
from handlers.users.narxi import get_price, price
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.storage import FSMContext
from keyboards.default.asos import asosiy

@dp.message_handler(text='Savatcha')
async def korzina(message: types.Message, state: FSMContext):
    try:
        products = db.get_products(tg_id=message.from_user.id)
        if len(products) == 0:
            await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")
        else:
            await anketa.savat0.set()
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("Buyurtma berish 🚚")
            products = db.get_products(tg_id=message.from_user.id)
            total = 0
            msg = "Savatcham:\n\n"
            nb = 1
            for product in products:
                products = db.get_products(tg_id=message.from_user.id)
                markup.add(f"❌ {product[1]} ❌")
                pricee = get_price(product[1], product[2])
                total += pricee    
                msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
                nb += 1

            msg += f"\nJami: {total} so'm"
            markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
            await message.answer(msg, reply_markup=markup, parse_mode='html')
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")

@dp.message_handler(text='Savatcha 🛒', state=anketa.category)
async def korzina(message: types.Message):
    try:
        products = db.get_products(tg_id=message.from_user.id)
        if len(products) == 0:
            await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")
        else:
            await anketa.savat.set()
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("Buyurtma berish 🚚")
            products = db.get_products(tg_id=message.from_user.id)
            total = 0
            msg = "Savatcham:\n\n"
            nb = 1
            for product in products:

                markup.add(f"❌ {product[1]} ❌")
                pricee = get_price(product[1], product[2])
                total += pricee    
                msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
                nb += 1

            msg += f"\nJami: {total} so'm"
            markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
            await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")

# @dp.message_handler(text='Savatcha 🛒', state=anketa.category)
# async def korzina(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     try:
#         msg = "Sizning buyutmalaringiz\n"
#         total = 0
#         if 'cart' in data.keys():
#             cart = data['cart']
#             for c in cart:
#                 narx = get_price(c['name'], c['amount'])
#                 msg += f"{c['name']} x {c['amount']} = {narx} so'm\n"
#                 total += narx
#         msg += f"\nUmumiy narx: {total} so'm"
#         await message.answer(msg)
#     except:
#         await message.answer("Savatchangiz bo'sh biror nima buyurtirmaysizmi?")




@dp.message_handler(text='Savatcha 🛒', state=anketa.product)
async def korzina(message: types.Message):
    try:
        products = db.get_products(tg_id=message.from_user.id)
        if len(products) == 0:
            await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")
        else:
            await anketa.savat2.set()
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("Buyurtma berish 🚚")
            products = db.get_products(tg_id=message.from_user.id)
            total = 0
            msg = "Savatcham:\n\n"
            nb = 1
            for product in products:
                markup.add(f"❌ {product[1]} ❌")
                pricee = get_price(product[1], product[2])
                total += pricee    
                msg += f"<b>{nb}.{product[1]}</b>\n<code>{price[product[1]]} X {product[2]} = {pricee} so'm</code>\n"
                nb += 1

            msg += f"\nJami: {total} so'm"
            markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
            await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")
    

        
    
    


# @dp.message_handler(text='Savatcha 🛒', state=anketa.product)
# async def korzina(message: types.Message, state: FSMContext):
#     idd = message.from_user.id
#     with open(file=f'E:/NG/Mirzobek_py/Botlar/Malumotlar/{idd}.txt', mode='r') as fayl:
#         r = fayl.read()
#         await message.answer(r)