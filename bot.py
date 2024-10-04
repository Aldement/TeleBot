import config
import asyncio
import random
import telebot.util
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)

jokes = [
    "Почему компьютер не может завести машину? Потому что он не может найти драйвер!",
    "Что сказал нулю восьмерка? Какой у тебя классный пояс!",
    "Почему программисты не ходят в лес? Потому что они боятся ошибок в коде.",
    "Я написал программу для приготовления кофе. Она не работает, но код выглядит вкусно!",
    "Зачем программист переходит дорогу? Чтобы закодировать новую сторону!"
]


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, я Эхобот! \nНапиши мне что нибудь, и я повторю это!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

@bot.message_handler(commands=['info'])
async def send_info(message):
    text = 'Это бот, который повторяет ваши сообщения. Напишите что-нибудь, и я повторю!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['joke'])
async def send_joke(message):
    joke = random.choice(jokes)
    await bot.reply_to(message, joke)

@bot.message_handler(commands=['coin'])
async def coin_handler(message):
    coin = random.choice(["ОРЕЛ", "РЕШКА"])
    await bot.reply_to(message, coin)

class Singer:
    def __init__(self, name, age, country, group, style_of_music, best_song, views):
        self.name = name
        self.age = age
        self.country = country
        self.group = group
        self.style_of_music = style_of_music
        self.best_song = best_song
        self.views = views

    def team(self):
        return f"{self.name} состоит в группе {self.group}, которая играет {self.style_of_music}."

    def popular_song(self):
        return f"Самая популярная песня — {self.best_song}, которая имеет {self.views} просмотров."

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Страна: {self.country}."


@bot.message_handler(commands=['singer'])
async def handle_car_command(message):
    args = telebot.util.extract_arguments(message.text)
    
    
    try:
        name, age, country, group, style_of_music, best_song, views = args.split()
    except ValueError:
        bot.reply_to(message, "Пожалуйста, используйте формат: /singer <имя> <возвраст> <страна> <группа> <стиль музыки> <лучшая песня> <просмотры лучшей песни>")
        return

    singer = Singer(name=name, age=age, country=country, group=group, style_of_music=style_of_music, best_song=best_song, views=views)

    await bot.reply_to(message, singer.info())
    await bot.reply_to(message, singer.team())
    await bot.reply_to(message, singer.popular_song())

asyncio.run(bot.polling())