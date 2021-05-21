import os
# import discord
from replit import db

from discord.ext import commands

# Models
from models import Gathering

# Not needed for repl.it
# from dotenv import load_dotenv
# load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Required to access list of members. Must also check boxes in bot permmissions
# intents = discord.Intents.all()
# client = discord.Client(intents=intents)

# initialize gatherings
if 'gatherings' not in db:
    db['gatherings'] = []

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='list', help='list all gatherings')
async def list_gatherings(ctx):
    if len(db['gatherings']) == 0:
        await ctx.send('no gatherings listed')
    else:
        gatherings = [
            Gathering(gathering_data) for gathering_data in db['gatherings']
        ]
        await ctx.send('\n'.join(gatherings))

bot.run(TOKEN)
