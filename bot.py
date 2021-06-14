import os
# import discord
from replit import db

from discord.ext import commands

# Models
from models import Gathering
from models import Topics

# Util
import util

# Not needed for repl.it
# from dotenv import load_dotenv
# load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Required to access list of members. Must also check boxes in bot permmissions
# intents = discord.Intents.all()

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
            print(len(db['gatherings']))
            gatherings = [
                Gathering(gathering_data)
                for gathering_data in db['gatherings']
            ]
            if only_open:
                gatherings = list(
                    filter(lambda gathering: (gathering.isOpen()), gatherings)
                )
            await ctx.send(
                '\n'.join([gathering.__str__() for gathering in gatherings])
            )

    async def select_topics(self, ctx, length):
        def check(msg):
            if (msg.author == ctx.author) and (msg.channel == ctx.channel):
                return True
            else:
                return False

        available_topics = Topics(Topics.all_topics)
        result_list = []
        while len(result_list) < length:
            await ctx.send(
                'Type the number corresponding to the topic to select it:\n{0}'
                .format(available_topics.pprint())
            )
            msg = await bot.wait_for('message', check=check)
            index = util.str_to_int(msg.content)
            if index > len(available_topics) - 1:
                raise ValueError(
                    "Your selection must be between 1 and {0}".
                    format(len(available_topics) - 1)
                )
            result_list.append(available_topics[index])
            available_topics.remove(index)
        await ctx.send(f'Your selections are: {", ".join(result_list)}')


bot = Bot()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='list', help='Lists all Circles')
async def list_gatherings(ctx):
    await bot.list_gatherings(ctx)


@bot.command(name='list open', help='Lists circles with availability')
async def list_open_gatherings(ctx):
    await bot.list_gatherings(ctx, only_open=True)


@bot.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(name='create', help='Create a new Circle')
async def create_gathering(ctx):
    def check(message):
        if (message.author == ctx.author) and (message.channel == ctx.channel):
            return True
        else:
            return False
    data = {}
    await ctx.send('Type a name for your Circle:')
    msg = await bot.wait_for('message', check=check)
    if Gathering.isValidName(msg.content):
        data['name'] = msg.content
    await ctx.send(f'Choose a date and time in the format MM-DD-YYYY HH:MM')
    msg = await bot.wait_for('message', check=check)
    data['date_time'] = Gathering.formatDate(msg.content)
    await ctx.send(f'Number of participants:')
    msg = await bot.wait_for('message', check=check)
    if Gathering.isValidTotalSeats(msg.content):
        data['total_seats'] = int(msg.content)
    await ctx.send(f'Time per topic in minutes:')
    msg = await bot.wait_for('message', check=check)
    if Gathering.isValidTime(msg.content):
        data['time_per_topic'] = int(msg.content)
    await ctx.send(f'Number of topics (3 recommended):')
    msg = await bot.wait_for('message', check=check)
    if Gathering.isValidNumberofTopics(msg.content):
        number_of_topics = int(msg.content)
        data['number_of_topics'] = number_of_topics
    await ctx.send(f'Select topics:')
    await bot.select_topics(ctx, number_of_topics)
    data['users'] = [{'name': ctx.author.name, 'id': ctx.author.id}]
    return db['gatherings'].append(data)

bot.run(TOKEN)
