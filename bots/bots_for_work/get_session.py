from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Замените значения ниже своими данными API ID и API Hash
api_id = '28598953'
api_hash = 'f8eeb037839642c35f9eaf9b3ad1693c'

# Создайте сессию с помощью StringSession
with TelegramClient(StringSession(), api_id, api_hash) as client:
    # Получите session_string
    session_string = client.session.save()
    print(session_string)