#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import os
from gpiozero import LED
import telebot

led = LED(17)

API_TOKEN = '5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['on'])
def send_welcome(message):
    led.on()
    bot.reply_to(message, """\
Encendido\
""")

@bot.message_handler(commands=['off'])
def send_welcome(message):
    led.off()
    bot.reply_to(message, """\
Apagado\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()