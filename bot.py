import os
# import discord
from dotenv import load_dotenv
from replit import db

from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Required to access list of members. Must also check boxes in bot permmissions
# intents = discord.Intents.all()
# client = discord.Client(intents=intents)

# initialize gatherings
if 'gatherings' not in db:
    db['gatherings'] = []

bot = commands.Bot(command_prefix='!')


@bot.command(name='list', help='list all gatherings')
async def list_gatherings(ctx):
    return

bot.run(TOKEN)
