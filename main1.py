import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from button import menu
from states import Anketa
import re


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def do_start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}", reply_markup=menu)
    

@dp.message_handler(text="Anketa to'ldirish")
async def start_anketa(message: types.Message):
    await message.answer("Ismingizni kiriting")
    await Anketa.ism.set()


@dp.message_handler(state=Anketa.ism)
async def get_ism(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(
        {'ism': ism}
    )
    await message.answer("Familiyangizni kiriting")
    await Anketa.next()

@dp.message_handler(state=Anketa.familiya)
async def get_fam(message: types.Message, state: FSMContext):
    familiya = message.text
    await  state.update_data(
        {'familiya': familiya}
    )
    await message.answer("Emailingizni kiriting:")
    await Anketa.next()


eml = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
@dp.message_handler(state=Anketa.email)
async def get_ism(message: types.Message, state: FSMContext):
    email = message.text
    if re.match(eml, email):
        await state.update_data(
            {'email': email}
        )
        await message.answer("Telefon raqamingizni kiriting:")
        await Anketa.next()
    else:
        await message.answer("Emailni to'g'ri kiriting!")
        await Anketa.email
    

num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
@dp.message_handler(state=Anketa.phone)
async def get_ism(message: types.Message, state: FSMContext):
    phone = message.text
    if re.match(num, phone):
        await state.update_data(
    {'Telefon raqam': phone}
    )
    else:
        await message.answer("Telefon raqamni to'g'ri kiriting!")
        await Anketa.phone
    await state.update_data(
        {'Telefon raqam': phone}
    )
    data = await state.get_data()

    fname = data.get("ism")
    lname = data.get('familiya')
    tel = data.get('Telefon raqam')
    eml = data.get('email')
    await message.answer(f"Quyidagilar qabul qilindi\nIsm: {fname}\nFamiliya: {lname}\nTelefon: {tel}\nemail: {eml}")
    await state.finish()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)