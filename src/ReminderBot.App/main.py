#bot.py
import os 
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')   

def get_prefix(bot, message):
    prefixes = ['!', '?', '-', '.', '>']

    if not message.guild:
        return '!'
    
    return commands.when_mentioned_or(*prefixes)(bot, message)

extensions = ['cogs.general']
bot = commands.Bot(command_prefix = get_prefix, description='Reminder Bot')

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as :{bot.user.name} - {bot.user.id} \nVersion:{discord.__version__}\n')

    await bot.change_presence(activity=discord.Activity(name='Running', type=1))
    print(f'Logged in and booted!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error)
    else:
        await ctx.send(error)

bot.run(TOKEN, bot = True, reconnect = True)