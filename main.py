import discord
import random
from discord.ext import commands
from spamd import spamm
import os
import requests
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    """just say hello and name"""
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    """Says he as many times as you say"""
    await ctx.send("he" * count_heh)

@bot.command()
async def calc(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def spam(ctx):
    """spamming in chat random letters"""
    await ctx.send(spamm())
    
@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    # А вот так можно подставить имя файла из переменной!
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):
    mems2 = os.listdir('imagesanimal')
    images_name = random.choice(mems2)
    with open(f'imagesanimal/{images_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("token")
