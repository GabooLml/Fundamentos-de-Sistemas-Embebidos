from telebot.async_telebot import AsyncTeleBot
import asyncio
import Musica

bot = AsyncTeleBot('5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
async def send_welcome(message):
    Musica.init()
    await bot.reply_to(message, """\
Reproductor de musica
Gatita
Tití\
""")
    
# Handle '/start' and '/help'
@bot.message_handler(commands=['Gatita'])
async def send_welcome(message):
    Musica.stop()
    Musica.Gatita()
    await bot.reply_to(message, """\
Reproduciendo Gatita de Bellakath\
""")
    
@bot.message_handler(commands=['Titi'])
async def send_welcome(message):
    Musica.stop()
    Musica.Titi()
    await bot.reply_to(message, """\
Reproduciendo Titi de Bad Bunny\
""")
    
@bot.message_handler(commands=['Cochinae'])
async def send_welcome(message):
    Musica.stop()
    Musica.Cochinae()
    await bot.reply_to(message, """\
Reproduciendo Titi de Bad Bunny\
""")
    
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