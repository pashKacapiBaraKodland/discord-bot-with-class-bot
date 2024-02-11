import discord
import random
from discord.ext import commands
from spamd import spamm
import os

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
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
    mems = os.listdir('images')
    img_name = random.choice(mems)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
@bot.command()
async def animal(ctx):
    mems2 = os.listdir('imagesanimal')
    images_name = random.choice(mems2)
    with open(f'imagesanimal/{images_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


bot.run("token")
