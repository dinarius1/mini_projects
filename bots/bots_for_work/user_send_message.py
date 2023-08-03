


from telethon.sync import TelegramClient
from telethon.sessions import StringSession

session_string = config('YOUR_STRING_SESSION')
api_id = '28598953'
api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'  # Замените это на ваш String Session, полученный на шаге 3

# Функция для отправки сообщения пользователю по его айди
def send_message_to_user(user_id, message):
    with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        client.send_message(user_id, message)

# Список айди пользователей, которым вы хотите отправить сообщения
user_ids = [6229644331]  # Добавьте больше айди пользователей при необходимости

# Сообщение, которое вы хотите отправить
message_to_send = "Привет! Это автоматическое сообщение от Python."

# Отправляем сообщение каждому пользователю из списка
for user_id in user_ids:
    send_message_to_user(user_id, message_to_send)

print("Сообщения успешно отправлены!")