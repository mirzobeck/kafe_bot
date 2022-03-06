from aiogram.types import ReplyKeyboardMarkup




menyu = ReplyKeyboardMarkup(resize_keyboard=True)
menyu.row("ORQAGA ↩️", "Savatcha 🛒")
menyu.row("Shashlik","Baliq 🐠")
menyu.row("Холодные закуски", "Salatlar")
menyu.row("Ichimliklar 🥤", "Sho'rva")


Shashlik = ReplyKeyboardMarkup(resize_keyboard=True)
Shashlik.row("ORQAGA ↩️", "Savatcha 🛒")
Shashlik.row("Kuskavoy (mol go'shti)", "Kuskavoy (qo'y go'shti)")
Shashlik.row("Rulet", "2 ichida 1")
Shashlik.row("Napoleon", "Qiymali kabob")

prod = ReplyKeyboardMarkup(resize_keyboard=True)
prod.row("1","2","3")
prod.row("4","5","6")
prod.row("7","8","9")
prod.row("ORQAGA ↩️")


balq = ReplyKeyboardMarkup(resize_keyboard=True)
balq.row("ORQAGA ↩️", "Savatcha 🛒")
balq.row("Sazan (300g)", "Sudak (300g)")
balq.row("Sous 300ml", "Sous 500ml")
balq.row("Bosh Sahifa 🏠")


zaquska = ReplyKeyboardMarkup(resize_keyboard=True)
zaquska.row("ORQAGA ↩️", "Savatcha 🛒")
zaquska.row("Suzma", "Ruscha Seld balig'i")
zaquska.row("Assorti", "Xolodes")
zaquska.row("Assorti (tuzli)", "Свежие нарезки")


salat = ReplyKeyboardMarkup(resize_keyboard=True)
salat.row("ORQAGA ↩️", "Savatcha 🛒")
salat.row("Olivye", "Smak")
salat.row("Cesar", "Fransuzcha")
salat.row("Mimoza", "Селёдка под шубой")


water = ReplyKeyboardMarkup(resize_keyboard=True)
water.row("ORQAGA ↩️", "Savatcha 🛒")
water.row("Coca-Cola (0,5 L)", "Coca-Cola (1,0 L)")
water.row("Coca-Cola (1,5 L)", "Fanta (0,5 L)")
water.row("Fanta (1,0 L)", "Fanta (1,5 L)")


shorva = ReplyKeyboardMarkup(resize_keyboard=True)
shorva.row("ORQAGA ↩️", "Savatcha 🛒")
shorva.row("Mastava", "Moshxurda")
shorva.row("Borsh", "Frikadelkali sho'rva")
shorva.row("Sho'rva(mol go'shti)", "Solyanka")