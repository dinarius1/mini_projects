









#
# from telethon.sync import TelegramClient
# from telethon.sessions import StringSession
# import csv
# from decouple import config
#
# # Получите значения YOUR_STRING_SESSION из конфигурационного файла или другим способом
# session_string = config('YOUR_STRING_SESSION')
# api_id = '28598953'
# api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'
#
# # Функция для отправки сообщения пользователю от вашего аккаунта
# def send_message_to_user(user_id, message):
#     with TelegramClient(StringSession(session_string)) as client:
#         client.send_message(user_id, message)
#
# # Функция для чтения айди пользователей из файла CSV и отправки сообщения
# def send_greetings_to_users_from_csv(filename, message):
#     with open(filename, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             user_id = int(row['user_id'])
#             send_message_to_user(user_id, message)
#
# # Пример использования
# if __name__ == "__main__":
#     filename = 'user_ids.csv'
#     message_to_send = "Привееееет!"
#     send_greetings_to_users_from_csv(filename, message_to_send)













#
# import telebot
# from decouple import config

# token = config('TOKEN')
# bot = telebot.TeleBot(token)

# # Получение списка подписчиков канала через Telegram API
# def get_channel_subscribers():
#     api_id = '28598953'
#     api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'
#     session_string = '1ApWapzMBu3mCdoqj6F1jwOFKbXudlRQd9WYhD0AMrxdIAgkx1c30XK0Oy1Ayfb_ucMBb-eEGfRuKYotcm5r2zkL6HbqsYg_tb5-UfW8Ub-bjIe6jIrabIr-rPjwtYxu_rjLf6dUAJzpoE3DqJiB-_JIcoo2wTpTXjAxlhn9V0IFfLLI2muGB84Ulu4eeG8qQvC-hw8n-K3Gtm9fEK9TQMZzjEEYhJ4V2CIgVNHPEdf_DmIWGpAWWa8Jo0mg7J1BxzM5XMWVTGEaufqruVXLapyEqRzfluFr24IFXeK9BnN3Id6EdI5meyb2ey1XaGrL_eo15ylxZo7IkZA7VBfaGv1UHoHtVU9Y='

#     client = TelegramClient(StringSession(session_string), api_id, api_hash)
#     client.start()

#     # Замените 'channel_username' на имя пользователя (или chat_id) вашего канала
#     channel_entity = client.get_entity(497209725)

#     # Получите список подписчиков канала
#     subscribers = client.get_participants(channel_entity)

#     client.disconnect()

#     return subscribers

# # Отправка сообщения пользователю по его user id
# def send_message_to_user(user_id, message):
#     bot.send_message(chat_id=user_id, text=message)

# # Пример использования
# def main():
#     subscribers = get_channel_subscribers()
#     message_to_send = "Привет!!!!"

#     for subscriber in subscribers:
#         user_id = subscriber.id
#         send_message_to_user(user_id, message_to_send)

# if __name__ == "__main__":
#     main()








