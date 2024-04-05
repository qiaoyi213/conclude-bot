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
async def clean(ctx):
    # clean chat_log file
    with open('../chat_log.txt', 'w') as f:
        f.write('')
    
    await ctx.send(f'已清理紀錄，接下來將從下一則訊息開始總結')

@bot.command()
async def conclude(ctx):
    # read chat_log file
    await ctx.send('總結中...')
    with open('../chat_log.txt', 'r') as f:
        chat_log = f.read()
    await ctx.send(GAI.conclude(chat_log))
    await clean(ctx)

@bot.command()
async def show_chat(ctx):
    # upload file to discord
    await ctx.send(file=discord.File(r'../chat_log.txt'))

@bot.event
async def on_message(message):
    # save message in chat_log file
    if len(message.content) > 0 and message.content[0] != '$':
        with open('../chat_log.txt', 'a') as f:
            f.write(f'{message.author.name}: {message.content}\n')
    await bot.process_commands(message)

bot.run(get_discord_token())

