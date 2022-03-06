from aiogram import types
from keyboards.default.catogory import Shashlik, balq,zaquska, salat, water, shorva
from loader import dp, db
from aiogram.dispatcher import FSMContext
from states.st import anketa
from handlers.users.narxi import price


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(state=anketa.amout)
async def orqa1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        od = data.get('odi')
        cat = data.get('cat')
        # nn = price[od]* int(n)
        if cat == 'Shashlik':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=Shashlik)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            
            await anketa.product.set()
        elif cat == 'Baliq 🐠':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=balq)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await anketa.product.set()
        elif cat == "Холодные закуски":
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=zaquska)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await anketa.product.set()
        elif cat == "Salatlar":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=salat)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await anketa.product.set()
        elif cat == "Ichimliklar 🥤":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=water)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await anketa.product.set()
        elif cat == "Sho'rva":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=shorva)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await anketa.product.set()
    else:
        await message.answer("Faqat son kiriting!")
        await anketa.amout.set()