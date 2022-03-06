
price = {
    'Sazan (300g)' : 45000,
    'Sudak (300g)' : 48000,
    'Sous 300ml' : 7000,
    'Sous 500ml' : 11000,
    "Kuskavoy (mol go'shti)" : 13500,
    "Kuskavoy (qo'y go'shti)" : 14000,
    'Rulet' : 17000,
    '2 ichida 1' : 14000,
    'Napoleon' : 17000,
    'Qiymali kabob' : 12500,
    "Suzma" : 7500,
    "Ruscha Seld balig'i" : 21000,
    "Assorti" : 72000,
    "Xolodes" : 17000,
    "Assorti (tuzli)" : 16000,
    "Свежие нарезки" : 15000,
    "Olivye" : 20000,
    "Smak" : 14000,
    "Cesar" : 20000,
    "Fransuzcha" : 21000,
    "Mimoza" : 24000,
    "Селёдка под шубой" : 24000,
    "Coca-Cola (0,5 L)" : 7000,
    "Coca-Cola (1,0 L)" : 11000,
    "Coca-Cola (1,5 L)" : 13000,
    "Fanta (0,5 L)" : 7000,
    "Fanta (1,0 L)" : 10000,
    "Fanta (1,5 L)" : 13000,
    "Mastava" : 16000,
    "Borsh" : 16000,
    "Frikadelkali sho'rva" : 15000,
    "Sho'rva(mol go'shti)" : 19000,
    "Solyanka" : 17000
    }


def get_price(name, amount):
    narx = price[name]
    return narx  * amount




