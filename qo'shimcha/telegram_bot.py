# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 20:17:04 2023

@author: Lenovo
"""

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '6089602143:AAElJbkv0G2NYTJpkBGBjYAS6-UGJrnEwRY'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum botimizga xush kelibsiz!"
#    javob += "\nLotincha matn yozsang krillchaga tarjima atib beraman "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    matn = message.text
    if matn.isascii():
        javob = to_cyrillic(matn)
    else:
        javob = to_latin(matn)
    bot.reply_to(message, javob)
    
bot.polling()