import telebot
from decouple import config
from buttons import keyboard
from utils import get_db

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):
    # print(message)
    bot.send_message(message.chat.id, 'Hello', reply_markup=keyboard) 

@bot.callback_query_handler(lambda x: True)
def send_data(call):
    db = get_db()
    page = call.data  #мы в utils писали команду callback data - это приводит к тому, что мы получаем какой то сигнал call, который выводит page (номер страиницы)
    products = db[page] #здесь по факту 
    for prod in products:
        text = f"""
Title: {prod['title']}
Price: {prod['price']}
"""
        bot.send_message(call.from_user.id, text)





bot.polling()
