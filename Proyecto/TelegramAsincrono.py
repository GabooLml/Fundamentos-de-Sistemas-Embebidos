"""Librerías que permiten la implementación del bot de Telegram de manera
asíncrona y la llamada del módulo reproductor de música
"""
from telebot.async_telebot import AsyncTeleBot
import asyncio
import Musica

#Token del bot empleado de Telegram
bot = AsyncTeleBot('5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk')

"""Comando que permite la inicialización del reproductor de musica y despliega
los titulos de algunas de ellas"""
# Handle '/help'
@bot.message_handler(commands=['help'])
async def send_welcome(message):
    Musica.init()
    await bot.reply_to(message, """\
Reproductor de musica
Gatita
Tití
Cochinae
""")

#Reproduce una canción
# Handle '/Gatita'
@bot.message_handler(commands=['Gatita'])
async def send_welcome(message):
    Musica.stop()
    Musica.Gatita()
    await bot.reply_to(message, """\
Reproduciendo Gatita de Bellakath\
""")

#Reproduce una canción
# Handle '/Titi'
@bot.message_handler(commands=['Titi'])
async def send_welcome(message):
    Musica.stop()
    Musica.Titi()
    await bot.reply_to(message, """\
Reproduciendo Titi de Bad Bunny\
""")

#Reproduce una canción
# Handle '/Cochinae'
@bot.message_handler(commands=['Cochinae'])
async def send_welcome(message):
    Musica.stop()
    Musica.Cochinae()
    await bot.reply_to(message, """\
Reproduciendo Cochinae de Julián Sosa\
""")

#Detiene la reproducción de música
# Handle '/Stop'
@bot.message_handler(commands=['stop'])
async def send_welcome(message):
    Musica.stop()
    await bot.reply_to(message, """\
Musica detenida\
""")
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

asyncio.run(bot.polling())