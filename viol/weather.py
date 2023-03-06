from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS 
import pandas as pd
import os
from creare_bot import dp, bot


import openai





@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    url = "https://rp5.ru/Погода_в_Омске"
    r = requests.get(url)
    soup = BS(r.text, "html.parser")
    temp = soup.find('span', class_="t_0")
    omsk_temperature = temp.text
    await bot.send_message(message.from_user.id, f'Погода в омске сейчас {temp.text}')


def commad_register_weath(dp : Dispatcher):
    dp.register_message_handler(weather, commands=['weather'])

