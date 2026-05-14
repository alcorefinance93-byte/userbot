from telethon import TelegramClient, events

API_ID = 35927138
API_HASH = "d9353b9787977fd56dcc43516d940733"
CHAT_A_ID = -1001999576082
CHAT_B_ID = -1003879261451

client = TelegramClient("session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHAT_A_ID))
async def forward(event):
    await client.forward_messages(CHAT_B_ID, event.message)

print("Userbot запущено!")
client.start()
client.run_until_disconnected()
