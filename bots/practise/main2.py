import telebot
from decouple import config
# config - функция, которая достает значение переменной в файле .env (пример, как должен выглядеть файл .env в файле .env - эта фунция позволяет в ДАННОМ СЛУЧАЕ не показывать на виду наш ключ Токен)


token = config('TOKEN')

bot = telebot.TeleBot(token)  #запускаем нашего бота

@bot.message_handler(commands=['start'])
# декоратор message_handler нужен, чтобы реагировать на определенные сообщения, данный декоратор уже встроен в bot (?)

# commands - встроенный параметр, представляющий список команд (функция работает, когда ползователь написал одну из них)


def start_message(message):
    bot.send_message(message.chat.id, 'Hello')  #вместо "message.chat.id" можно написать  892891195
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBRZkBXYLzRtuLYx8tQglxiZQ0WJ9_AACDQYAAtCG-wqBWgG-gkiB_S4E')
    bot.send_photo(message.chat.id, 'https://ru.freepik.com/free-photo/lavender-field-at-sunset-near-valensole_35758793.htm#query=landscape&position=0&from_view=keyword&track=sph')

bot.polling()
