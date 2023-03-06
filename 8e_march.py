from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
from creare_bot import dp, bot

import os
from viol import work_code, admin_command, weather


@dp.message_handler(commands=['start', 'help'])
async def start_commads(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я бот Сергея и я расскажу почему Виолетта лучшая.')
        await message.delete()
    except:
        await message.reply('Общение с ботом осуществляется через лс, напишите ему')



work_code.commad_register_hendler(dp)
weather.commad_register_weath(dp)

executor.start_polling(dp, skip_updates=True)
