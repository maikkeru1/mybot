import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8980556144:AAHuFoXEG1cwulFQLGZReuM8uoVf16N8Q80"  # ← вставьте токен сюда

AUTO_REPLY_TEXT = """
Warning: the Telegram account associated with this contact has been compromised and published
in a dox database. Ignore any previous or future messages sent from the affected account until ownership is verified.
"""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
replied_users: set[int] = set()

@dp.message()
async def handle_business_message(message: Message):
    if not message.business_connection_id:
        return
    user_id = message.from_user.id
    if user_id in replied_users:
        return
    if message.from_user.is_bot:
        return
    await message.reply(AUTO_REPLY_TEXT)
    replied_users.add(user_id)
    print(f"✅ Ответил: {message.from_user.full_name}")

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot, allowed_updates=["message", "business_message"])

if __name__ == "__main__":
    asyncio.run(main())
