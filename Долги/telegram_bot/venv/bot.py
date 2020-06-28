import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, """Хэлоу, {0.first_name}!\nМеня зовут <b>{1.first_name}</b>, 
    бот созданный для шуток над Санями""".format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Саня':
        number = random.randint(1, 12)
        mem = open('mem/'+str(number)+'.jpg', 'rb')
        bot.send_photo(message.chat.id, mem)


# Run
bot.polling(none_stop=True)
