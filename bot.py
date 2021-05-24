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

# bot = commands.bot(command_prefix='!')


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    async def list_gatherings(self, ctx, only_open=False):
        if len(db['gatherings']) == 0:
            await ctx.send('There are no Circles scheduled')
        else:
            gatherings = [
                Gathering(gathering_data)
                for gathering_data in db['gatherings']
            ]
            if only_open:
                gatherings = list(
                    filter(lambda gathering: (gathering.isOpen()), gatherings)
                )
            await ctx.send('\n'.join(gatherings))


bot = Bot()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='list', help='Lists all Circles')
async def list_gatherings(ctx):
    await bot.list_gatherings(ctx)
    # if len(db['gatherings']) == 0:
    #     await ctx.send('There are no Circles scheduled')
    # else:
    #     gatherings = [
    #         Gathering(gathering_data) for gathering_data in db['gatherings']
    #     ]
    #     await ctx.send('\n'.join(gatherings))


@bot.command(name='list open', help='Lists circles with availability')
async def list_open_gatherings(ctx):
    if len(db['gatherings']) == 0:
        await ctx.send('There are no Circles scheduled')
    else:
        all_gatherings = [
            Gathering(gathering_data) for gathering_data in db['gatherings']
        ]
        available_gatherings = list(
            filter(lambda gathering: (gathering.isOpen()), all_gatherings)
        )
        await ctx.send('\n'.join(available_gatherings))


@bot.command(name='create', help='Create a new Circle')
async def create_gathering(ctx):
    # await list_open_gatherings(ctx)
    await ctx.send('testing')

bot.run(TOKEN)
