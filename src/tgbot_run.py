import os
from telethon import TelegramClient, events

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")

bot = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    chat_id = event.chat_id  # Get chat ID
    user_id = event.sender_id  # Get user ID
    await event.respond("Hi!")
    raise events.StopPropagation


@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(event.text)


def main():
    """Start the bot."""
    bot.run_until_disconnected()
