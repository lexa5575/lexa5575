import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn = types.KeyboardButton("Глянуть что есть")
btn1 = types.KeyboardButton("Связаться с оператором")
btn2 = types.KeyboardButton("Поделиться ботом с друзьями")
keyboard1.add(btn, btn1, btn2)

keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn = types.KeyboardButton("☘️Шишка Amnesia Outlaw☘️")
btn1 = types.KeyboardButton("❄️       Амфетамин      ❄️")
btn2 = types.KeyboardButton("💎     Кристал 3 cmc    💎")
keyboard2.add(btn, btn1, btn2)

keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn = types.KeyboardButton("➖1️⃣ - 60 zł")
btn1 = types.KeyboardButton("➖ 3️⃣ - 170zł")
btn2 = types.KeyboardButton("➖5️⃣ - 270zł")
keyboard3.add(btn, btn1, btn2)

payGood = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn = types.KeyboardButton("Я оплатил")
btn1 = types.KeyboardButton("Связаться с оператором")
payGood.add(btn, btn1)

@bot.message_handler(commands=["start"])
def start(messege):
    bot.send_message(messege.chat.id,"Вас приветствует GoVegas market",
        parse_mode='html', reply_markup=keyboard1)
    return


@bot.message_handler(content_types=["text"])
def fierstText(message):
    if message.text == "Глянуть что есть":
        bot.send_message(message.chat.id, "Это все что у нас есть", parse_mode="html", reply_markup=keyboard2)
    elif message.text == "Связаться с оператором":
        bot.send_message(message.chat.id, "@GoodandGod")
    elif message.text == "Поделиться ботом с друзьями":
        bot.send_message(message.chat.id, "@call3bot  просто напиши так своему другу и порекомендуй нас!")
    elif message.text == "☘️Шишка Amnesia Outlaw☘️":
        bot.send_message(message.chat.id, "‼️Обновление‼️ Lemon Haze 🔞Про-во: 🇱🇺Тип: 80% Индика/ 20% СативаТГК: 25%"
                                          "Price:     ➖1️⃣ - 60 zł    ➖ 3️⃣ - 170zł     ➖5️⃣ - 270zł 💵 Оплата - BLIK / номер телефона.", reply_markup= keyboard3)
        bot.send_message(message.chat.id, "💵 Оплата - BLIK / номер телефона.")
        bot.register_next_step_handler(message, secondText)
    else:
        bot.send_message(message.from_user.id, "Просто нажмите на нужную кнопку возле клавиатуры", parse_mode="html")
        return

def secondText(message):
    if message.text == "➖1️⃣ - 60 zł":
        bot.send_message(message.from_user.id, "Вы получите 1 гр. за 60zł. Пожалуйста переведите"
                                               " точную сумму на номер кошелька 729456841,", parse_mode="html")
        bot.send_message(message.from_user.id, " Cразу после оплаты вы получите фотографию"
                                               " с точными кординатами клада", parse_mode="html", reply_markup= payGood)
        bot.register_next_step_handler(message, send_text)
    elif message.text == "➖ 3️⃣ - 170zł":
        bot.send_message(message.from_user.id, "Вы получите 3 гр. за 170zł. Пожалуйста переведите"
                                               " точную сумму на номер кошелька 729456841,", parse_mode="html")
        bot.send_message(message.from_user.id, " Cразу после оплаты вы получите фотографию"
                                               " с точными кординатами клада", parse_mode="html", reply_markup= payGood)
        bot.register_next_step_handler(message, send_text)
    elif message.text == "➖5️⃣ - 270zł":
        bot.send_message(message.from_user.id, "Вы получите 5 гр. за 270zł. Пожалуйста переведите"
                                               " точную сумму на номер кошелька 729456841"
                                               , parse_mode="html", reply_markup= payGood)
        bot.send_message(message.from_user.id, " Cразу после оплаты вы получите фотографию"
                                               " с точными кординатами клада", parse_mode="html", reply_markup= payGood)
        bot.register_next_step_handler(message, send_text)
    else:
        bot.send_message(message.from_user.id, "Просто нажмите на нужную кнопку возле клавиатуры", parse_mode="html")
        return

def send_text(message):
    if message.chat.type == 'private':
        if message.text == "Я оплатил":
            bot.send_message(message.from_user.id, "Секундочку, проверяю оплату.")
    elif message.text == "Связаться с оператором":
            bot.send_message(message.chat.id, "@GoodandGod")




bot.polling(none_stop=True)