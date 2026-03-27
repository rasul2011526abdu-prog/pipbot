import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Initialize bot and dispatcher
API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(dp):
    print('Bot is online')

if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=on_startup)