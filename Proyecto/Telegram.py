#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import os
import telebot
import RGB

API_TOKEN = '5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['off'])
def send_welcome(message):
    RGB.off_rgb()
    bot.reply_to(message, """\
Apagado
/help para más comandos\
""")

# Handle '/help'
@bot.message_handler(commands=['rojo'])
def send_help(message):
    RGB.set_red()
    bot.reply_to(message, """\
/on para encender la luz
/off para apagar la luz\
""")

@bot.message_handler(commands=['on'])
def send_notification_on(message):
    led.on()
    bot.reply_to(message, """\
Encendido\
""")

@bot.message_handler(commands=['off'])
def send_notification_off(message):
    led.off()
    bot.reply_to(message, """\
Apagado\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()