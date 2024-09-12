import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='c!', intents=intents)

async def on_ready(self):
    print(f'Logged on as {self.user}!')

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)
    
bot.run(os.getenv("TOKEN"))