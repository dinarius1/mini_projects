import telebot
from decouple import config
import os

token = config('TOKEN')
bot = telebot.TeleBot(token)

# ID вашего телеграмм канала
channel_id = -1001815322079  # Замените на ваш реальный ID канала

# Путь к файлу для хранения количества запусков
start_count_file = 'start_count.txt'

def increment_start_count():
    # Проверяем существование файла
    if os.path.exists(start_count_file):
        with open(start_count_file, 'r') as f:
            count = int(f.read())
    else:
        count = 0

    # Увеличиваем счетчик на 1
    count += 1

    # Записываем обновленное значение обратно в файл
    with open(start_count_file, 'w') as f:
        f.write(str(count))

    return count

def send_message_to_channel(channel_id, message):
    caption_text = "Привет! Это фотография для тебя."
    photo_path = '/home/user/python27/mini-projects/bots/bots_for_work/рис.jpg'
    with open(photo_path, 'rb') as photo_file:
        bot.send_photo(channel_id, photo_file, caption=caption_text)

@bot.message_handler(commands=['start'])
def start_message(message):
    caption_text = "Привет! Это фотография для тебя."
    photo_path = '/home/user/python27/mini-projects/bots/bots_for_work/рис.jpg'
    with open(photo_path, 'rb') as photo_file:
        bot.send_photo(message.chat.id, photo_file, caption=caption_text)

    count = increment_start_count()
    # bot.send_message(message.chat.id, f"Бот был запущен {count} раз.")

@bot.message_handler(commands=['post'])
def send_to_channel(message):
    user_id = message.from_user.id  # Получаем ID пользователя, который вызвал команду
    if user_id == 497209725:  # Замените YOUR_USER_ID на ваш реальный ID пользователя
        send_message_to_channel(channel_id, "Привет! Это сообщение из бота, отправленное в канал.")
    else:
        bot.reply_to(message, "Извините, у вас нет прав для выполнения этой команды.")

@bot.message_handler(commands=['count'])
def show_count(message):
    count = get_start_count()
    bot.send_message(message.chat.id, f"Бот был запущен {count} раз.")

def get_start_count():
    # Проверяем существование файла
    if os.path.exists(start_count_file):
        with open(start_count_file, 'r') as f:
            count = int(f.read())
            return count
    else:
        return 0

bot.delete_webhook()
bot.polling()