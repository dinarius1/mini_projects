import telebot

token='5852272465:AAEkvp5r23_unIxY5z-QYZdEfg8bgBaXQ7I'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Йоу!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIB-ZkBidqWUgLB2YuovQ1TMEAATeGFAgAAokAA_w8pBM2vuyOxa_Hri4E')