from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
import os
from creare_bot import dp, bot
from key import kb_work
from key import violetta_best_button
from aiogram.types import ReplyKeyboardRemove
from key import gpt_work


import openai

open_tok = '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'

openai.api_key = open_tok

@dp.message_handler(commands=['start', 'help', 'перейти_в_меню'])
async def start_commads(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я бот Сергея и я расскажу почему Виолетта лучшая, я умею показывать погоду и в меня встроен ChatGPT', reply_markup=kb_work)
    except:
        await message.reply('Общение с ботом осуществляется через лс, напишите ему')

@dp.message_handler(commands=['Использовать_GPT'])
async def start_gpt(message: types.Message):
    await bot.send_message(message.from_user.id, 'ChatGPT активен всегда, но у него есть ограничение по кол-ву сообщений в связи с политикой OpenAI', reply_markup=gpt_work)

@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    await bot.send_message(message.from_user.id, f'bot is work, {datetime.now()}' )


@dp.message_handler(commands=['violetta'])
async def violettaT(message: types.Message):
    await bot.send_message(message.from_user.id, 'Я могу представить 10 фактов, почему Виоелетта лучшая', reply_markup=violetta_best_button)

@dp.message_handler(commands=['закрыть_кнопки'])
async def violettaT(message: types.Message):
    await bot.send_message(message.from_user.id, 'хорошо', reply_markup=ReplyKeyboardRemove())




@dp.message_handler()
async def num_chat(message: types.Message):
    if message.text == '1':
        await bot.send_message(message.from_user.id, 'Во первых: она самая красивая во всем мире')
        photo1 = open('viol/violetta1.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo1)
    elif message.text == '2':
        await bot.send_message(message.from_user.id, 'Во вторых: она работящая')
        photo2 = open('viol/violetta2.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '3':
        await bot.send_message(message.from_user.id, 'В третьих: она очень милая')
        photo2 = open('viol/violetta3.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '4':
        await bot.send_message(message.from_user.id, 'В четвертых: она любит животных')
        photo2 = open('viol/violetta5.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '5':
        await bot.send_message(message.from_user.id, 'В пятых: она очень модная и стильная')
        photo2 = open('viol/violetta4.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '6':
        await bot.send_message(message.from_user.id, 'В шестых: она временами загадочная')
        photo2 = open('viol/violetta6.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '7':
        await bot.send_message(message.from_user.id, 'В седьмых: она умеет делать ремонт')
        photo2 = open('viol/violetta7.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '8':
        await bot.send_message(message.from_user.id, 'В восьмом: она любит поспать')
        photo2 = open('viol/violetta8.jpg', 'rb')
        photo8_1 = open('viol/violetta8_1.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
        await bot.send_photo(message.from_user.id, photo8_1)
    elif message.text == '9':
        await bot.send_message(message.from_user.id, 'В девятых: она хорошая мама')
        photo2 = open('viol/violetta9.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    elif message.text == '10':
        await bot.send_message(message.from_user.id, 'А вообще, она и без причины самая лучшая, и Сергей ее очень сильно любит')
        photo2 = open('viol/violetta10.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo2)
    else: 
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
        
        await message.answer(response['choices'][0]['text'])
        

    


def commad_register_hendler(dp: Dispatcher):
    dp.register_message_handler(start_commads, commands=['start', 'help'])
    dp.register_message_handler(status, commands=['status'])
    dp.register_message_handler(num_chat, )
    dp.register_message_handler(violettaT, commands=['violetta'])
    dp.message_handler(start_gpt, commands=['Использовать_GPT'])

   