import discord
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# this is a test command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(token)

