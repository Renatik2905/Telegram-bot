from config import token
import telebot
from random import choice
import random

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'Привет! Я бот. Как дела?')
    elif message.text.lower() == 'какой сегодня день?':
        day = datetime.datetime.now().strftime("%A")
        bot.reply_to(message, f'Сегодня {day}')
    else:
        bot.reply_to(message, 'Извините, я не понимаю ваш запрос')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'like':
        bot.send_message(call.message.chat.id, 'Спасибо за лайк!')
        bot.answer_callback_query(call.id, text='Вы поставили лайк')
    elif call.data == 'dislike':
        bot.send_message(call.message.chat.id, 'Жаль, что вам не понравилось :(')
        bot.answer_callback_query(call.id, text='Вы поставили дизлайк')

bot.infinity_polling()
