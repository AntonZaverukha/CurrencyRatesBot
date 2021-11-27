import json
import requests
import telebot
import os
from Rates import DBrequestNBU, DBrequestPrivat
from Rates import NBUdata, Privatdata
import telegram.ext

Token = "2112974591:AAF8BTQXVKLU21Cb1cParAaVBwjSbVGvJyM"
Url = "https://api.telegram.org/bot2112974591:AAF8BTQXVKLU21Cb1cParAaVBwjSbVGvJyM/".format(Token)

bot = telebot.TeleBot('2112974591:AAF8BTQXVKLU21Cb1cParAaVBwjSbVGvJyM')


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Розпочати')
    msg = bot.send_message(message.chat.id, text='Натисни кнопку в меню', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='USD', callback_data='first'))
    menu1.add(telebot.types.InlineKeyboardButton(text='EUR', callback_data='second'))
    menu1.add(telebot.types.InlineKeyboardButton(text='RUB', callback_data='third'))
    menu1.add(telebot.types.InlineKeyboardButton(text='PLN', callback_data='fourth'))
    menu1.add(telebot.types.InlineKeyboardButton(text='BTC', callback_data='fifth'))

    if message.text == 'Розпочати':
        msg = bot.send_message(message.chat.id, text ='Виберіть валюту', reply_markup = menu1)
        # msg = bot.send_message(message.chat.id, text =  reply_markup=menu1)


# def step2(call):
# if call.data == 'first':
#         msg = bot.send_message(call.message.chat.id, 'Нажми третью кнопку', reply_markup = menu2)
#         bot.register_next_step_handler(msg, step3)
#
# def step3(call):
#     if call.data == 'third':
#         msg = bot.send_message(call.message.chat.id, 'Конец')
#     else:
#         pass

bot.polling(none_stop=True)
