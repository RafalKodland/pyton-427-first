import discord
from discord.ext import commands
from pass_gen import generate_password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, l1 = 0, l2 = 0):
    await ctx.send(f"Wynik: {l1+l2}")

@bot.command()
async def password(ctx, length = 10):
    await ctx.send(f"Wygenerowane hasło: {generate_password(length)}")

bot.run("")