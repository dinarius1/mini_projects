import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')  #  892891195
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBRZkBXYLzRtuLYx8tQglxiZQ0WJ9_AACDQYAAtCG-wqBWgG-gkiB_S4E')
    bot.send_photo(message.chat.id, 'https://ru.freepik.com/free-photo/lavender-field-at-sunset-near-valensole_35758793.htm#query=landscape&position=0&from_view=keyword&track=sph')

@bot.message_handler(content_types=['text'])
def aaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет")
    else:
        bot.send_message(message.chat.id, "Сообщение не распознано")

@bot.message_handler(content_types=['sticker'])
def bbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)

bot.polling()


