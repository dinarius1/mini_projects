
import  datetime
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from decouple import config
from telethon.tl.types import PeerChannel

session_string = config('YOUR_STRING_SESSION')
api_id = '28598953'
api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'  # Замените это на ваш String Session, полученный на шаге 3

# Создаем клиент Telegram
client = TelegramClient(StringSession(session_string), api_id, api_hash)
# channel_id = PeerChannel
# Входим в аккаунт
client.start()exist python library which allow to use whatsapp

from telethon import functions, types

with client:
    result = client(functions.channels.GetFullChannelRequest(
        channel='dordoitextile'
    ))
    print(result.stringify())



    # result = client(functions.messages.CreateChatRequest(
    #     users=['Vorobushek312'],
    #     title='My awesome title',
    #     # ttl_period=42
    # ))
    # print(result.stringify())
    #
    # # Does it have an username? Use it!
    # dialogs = client.get_dialogs()



# async def handler(event):
#     # This method may make a network request to find the input sender.
#     # Properties can't make network requests, so we need a method.
#     sender = await event.get_input_sender()
#     await client.send_message(sender, 'Hi')
#     await client.send_message(sender, 'Hi')
# async def handler(event):
#     await client.send_message(event.sender_id, 'Hi')
#     friend = await event.get_entity(5367541503)
#     print(friend)
    # friend.send_message(5367541503, 'Thanks for the Telethon library!')
    # print((friend))
    # client.send_message(1071339430, 'Thanks for the Telethon library!')
    # print(c)
client.disconnect()