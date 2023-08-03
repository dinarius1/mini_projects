import telebot
from decouple import config
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import csv

# Получите токен бота и идентификатор канала из конфигурационного файла
token = config('TOKEN')
bot = telebot.TeleBot(token)

# Получение списка подписчиков канала через Telegram API
def get_channel_subscribers():
    api_id = '28598953'
    api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'
    session_string = '1ApWapzMBu3mCdoqj6F1jwOFKbXudlRQd9WYhD0AMrxdIAgkx1c30XK0Oy1Ayfb_ucMBb-eEGfRuKYotcm5r2zkL6HbqsYg_tb5-UfW8Ub-bjIe6jIrabIr-rPjwtYxu_rjLf6dUAJzpoE3DqJiB-_JIcoo2wTpTXjAxlhn9V0IFfLLI2muGB84Ulu4eeG8qQvC-hw8n-K3Gtm9fEK9TQMZzjEEYhJ4V2CIgVNHPEdf_DmIWGpAWWa8Jo0mg7J1BxzM5XMWVTGEaufqruVXLapyEqRzfluFr24IFXeK9BnN3Id6EdI5meyb2ey1XaGrL_eo15ylxZo7IkZA7VBfaGv1UHoHtVU9Y='

    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    client.start()

    # Замените 'channel_username' на имя пользователя (или chat_id) вашего канала
    channel_entity = client.get_entity('dordoitextile')

    # Получите список ID подписчиков канала
    subscribers = client.get_participants(channel_entity)

    client.disconnect()

    return subscribers
# Запись имен пользователей в файл CSV
def write_usernames_to_csv(subscribers):
    with open('usernames.csv', 'w', newline='') as csvfile:
        fieldnames = ['username']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for subscriber in subscribers:
            if subscriber.username:
                writer.writerow({'username': subscriber.username})

# Пример использования
def main():
    subscribers = get_channel_subscribers()
    write_usernames_to_csv(subscribers)

if __name__ == "__main__":
    main()

# # Запись айди пользователей в файл CSV
# def write_user_ids_to_csv(subscribers):
#     with open('user_ids.csv', 'w', newline='') as csvfile:
#         fieldnames = ['user_id']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for subscriber in subscribers:
#             writer.writerow({'user_id': subscriber.id})
#
# # Пример использования
# def main():
#     subscribers = get_channel_subscribers()
#     write_user_ids_to_csv(subscribers)
#
# if __name__ == "__main__":
#     main()

# import telebot
# from decouple import config
# from telethon.sync import TelegramClient
# from telethon.sessions import StringSession
#
# # Получите токен бота и идентификатор канала из конфигурационного файла
# token = config('TOKEN')
# bot = telebot.TeleBot(token)
#
# # Замените "CHANNEL_ID" на идентификатор вашего канала
# channel_id = config('CHANNEL_ID')
#
# # Получение списка подписчиков канала через Telegram API
# def get_channel_subscribers():
#     api_id = '28598953'
#     api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'
#     session_string = '1ApWapzMBu3mCdoqj6F1jwOFKbXudlRQd9WYhD0AMrxdIAgkx1c30XK0Oy1Ayfb_ucMBb-eEGfRuKYotcm5r2zkL6HbqsYg_tb5-UfW8Ub-bjIe6jIrabIr-rPjwtYxu_rjLf6dUAJzpoE3DqJiB-_JIcoo2wTpTXjAxlhn9V0IFfLLI2muGB84Ulu4eeG8qQvC-hw8n-K3Gtm9fEK9TQMZzjEEYhJ4V2CIgVNHPEdf_DmIWGpAWWa8Jo0mg7J1BxzM5XMWVTGEaufqruVXLapyEqRzfluFr24IFXeK9BnN3Id6EdI5meyb2ey1XaGrL_eo15ylxZo7IkZA7VBfaGv1UHoHtVU9Y='
#
#
#     client = TelegramClient(StringSession(session_string), api_id, api_hash)
#     client.start()
#
#     # Замените 'channel_username' на имя пользователя (или chat_id) вашего канала
#     channel_entity = client.get_entity(-1001937065969)
#
#     # Получите список ID подписчиков канала
#     subscribers = client.get_participants(channel_entity)
#
#     client.disconnect()
#
#     return subscribers
#
# # Отправка сообщения пользователю по его user id
# def send_message_to_user(user_id, message):
#     bot.send_message(chat_id=user_id, text=message)
#
# # Пример использования
# def main():
#     subscribers = get_channel_subscribers()
#     message_to_send = "Привет! Это тестовое сообщение от бота."
#
#     for subscriber in subscribers:
#         user_id = subscriber.id
#         print(user_id)
#         # send_message_to_user(user_id, message_to_send)
#
# if __name__ == "__main__":
#     main()



# Замените значения ниже своими данными API ID, хешем сессии и токеном доступа
# api_id = '28598953'
# api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'
# session_string = '1ApWapzMBu3mCdoqj6F1jwOFKbXudlRQd9WYhD0AMrxdIAgkx1c30XK0Oy1Ayfb_ucMBb-eEGfRuKYotcm5r2zkL6HbqsYg_tb5-UfW8Ub-bjIe6jIrabIr-rPjwtYxu_rjLf6dUAJzpoE3DqJiB-_JIcoo2wTpTXjAxlhn9V0IFfLLI2muGB84Ulu4eeG8qQvC-hw8n-K3Gtm9fEK9TQMZzjEEYhJ4V2CIgVNHPEdf_DmIWGpAWWa8Jo0mg7J1BxzM5XMWVTGEaufqruVXLapyEqRzfluFr24IFXeK9BnN3Id6EdI5meyb2ey1XaGrL_eo15ylxZo7IkZA7VBfaGv1UHoHtVU9Y='
#
# # Создайте Telegram клиента и авторизуйтесь
# client = TelegramClient(StringSession(session_string), api_id, api_hash)
# client.start()
#
# # Замените 'channel_username' на имя пользователя (или chat_id) вашего канала
# channel_entity = client.get_entity(-1001937065969)
#
# # Получите список ID подписчиков канала
# subscribers = client.get_participants(channel_entity)
#
# # Выведите ID подписчиков канала
# for subscriber in subscribers:
#     print(subscriber.id)
#
# # Завершите сеанс
# client.disconnect()