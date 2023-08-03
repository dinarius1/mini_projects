
import  datetime
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from decouple import config
import csv
import time

session_string = config('YOUR_STRING_SESSION')
api_id = '28598953'
api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'  # Замените это на ваш String Session, полученный на шаге 3

# Создаем клиент Telegram
client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Входим в аккаунт
client.start()

from telethon import functions, types

with open('usernames.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    usernames = [row[0] for row in reader]

for username in usernames[14:21]:
    with client:
        result = client(functions.messages.SendMessageRequest(
            peer= username,
            message='Здравствуйте, высылаем вам коммерческое предложение в целях дальнейшего сотрудничества!🤝' +
                    '\nЗакажите свою линейку верхней женской одежды оптом по низким ценам.' + '\n'
                    '\nБудем рады обратной связи после ознакомления с коммерческим предложением.' + '\n'
                    '\n' + 'https://telegra.ph/Bems-Collection-Optom-07-26' + '!',
            no_webpage=True,
            noforwards=True,
            update_stickersets_order=True,
            top_msg_id=42,
            # schedule_date=datetime.datetime(2023, 7, 21),
            # send_as='aidina_work'
        ))
        print(result.stringify())
        time.sleep(60)

client.disconnect()

# with open('user_ids.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     usernames = [row[0] for row in reader]
# username =
# with client:
#     result = client(functions.messages.SendMessageRequest(
#         peer= username,
#         message='Здравствуйте, высылаем вам коммерческое предложение в целях дальнейшего сотрудничества!🤝' +
#                 '\nЗакажите свою линейку верхней женской одежды оптом по низким ценам.' + '\n'
#                 '\nБудем рады обратной связи после ознакомления с коммерческим предложением.' + '\n'
#                 '\n' + 'https://telegra.ph/Bems-Collection-Optom-07-26' + '!',
#         no_webpage=True,
#         noforwards=True,
#         update_stickersets_order=True,
#         top_msg_id=42,
#         # schedule_date=datetime.datetime(2023, 7, 21),
#         # send_as='aidina_work'
#     ))
#     print(result.stringify())
#
# client.disconnect()