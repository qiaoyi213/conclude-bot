import discord
from util import get_discord_token, get_openai_api_key
from discord.ext import commands
from openai_controller import openai_controller

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
GAI = openai_controller(get_openai_api_key())

@bot.event
async def on_ready():
    print(">> Bot is ready <<")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def test(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')

@bot.command()
async def conclude_all(ctx):
    await ctx.send(GAI.conclude_all())
    await ctx.send(GAI.conclude())

bot.run(get_discord_token())

