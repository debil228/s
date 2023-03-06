from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
import os
from creare_bot import dp, bot

@dp.message_handler(commands='status')
async def status(message: types.Message):
    await bot.send_message(message.from_user.id, f'bot is work, {datetime.now()}' )

