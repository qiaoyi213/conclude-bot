import discord
from util import get_discord_token
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is ready <<")

bot.run(get_discord_token())

