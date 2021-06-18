import os
import time
from replit import db
import discord

# Models
from models import Gathering, User

# Util
import util

# Bot
from bot import scheduling_bot as bot


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Required to access list of members. Must also check boxes in bot permmissions
# intents = discord.Intents.all()

# initialize gatherings
if 'gatherings' not in db:
    db['gatherings'] = []


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='list', help='Lists all Circles')
async def list_gatherings(ctx):
    try:
        await bot.list_gatherings(ctx)
    except (ValueError, IndexError) as e:
        await ctx.send(f'Error: {str(e)}')


@bot.command(name='list open', help='Lists circles with availability')
async def list_open_gatherings(ctx):
    try:
        await bot.list_gatherings(ctx, only_open=True)
    except (ValueError, IndexError) as e:
        await ctx.send(f'Error: {str(e)}')


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
    try:
        data = {}
        await ctx.send('Type a name for your Circle:')
        msg = await bot.wait_for('message', check=check)
        if Gathering.isValidName(msg.content):
            data['name'] = msg.content
        await ctx.send(
            f'Choose a date and time in the format MM-DD-YYYY HH:MM'
        )
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
        data['topics'] = await bot.select_topics(ctx, number_of_topics)
        data['users'] = [{'name': ctx.author.name, 'id': ctx.author.id}]
        gathering = Gathering(data)
        await ctx.send('Circle Created! Type "!list" to view all Circles:')
        await ctx.send(gathering.toString())
        db['gatherings'].append(data)
        time.sleep(2)
        await ctx.invoke(bot.get_command('clear'))
    except (ValueError, IndexError) as e:
        await ctx.send(f'Error: {str(e)}')


@bot.command(name='join', help='Join an open circle')
async def join_gathering(ctx):
    def check(message):
        if (message.author == ctx.author) and (message.channel == ctx.channel):
            return True
        else:
            return False
    try:
        gatherings = []
        for gathering_data in db['gatherings']:
            gathering = Gathering(gathering_data)
            if gathering.isOpen():
                gatherings.append(gathering)
        await ctx.send(
            'Type the number of the circle you want to join:\n{0}'
            .format(bot.pprint_gatherings(gatherings))
        )
        msg = await bot.wait_for('message', check=check)
        index = util.str_to_int(msg.content)
        if (index > len(gatherings) - 1) or index < 0:
            raise ValueError('Number is out of range')
        gathering = gatherings[index]
        user = User({'name': ctx.author.name, 'id': ctx.author.id})
        if user not in gathering.users:
            gathering.users.append(user)
    except (ValueError, IndexError) as e:
        await ctx.send(f'Error: {str(e)}')


# Delete all messages that don't start with '!'
@bot.event
async def on_message(message):
    scheduling_channel = discord.utils.get(
        bot.get_all_channels(), name='schedule-a-coin-session'
    )
    if (message.channel == scheduling_channel) and not (
        message.content.startswith('!')
    ):
        await message.delete(message)


bot.run(TOKEN)
