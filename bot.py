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

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Goldfire server!'
    )

bot.run(TOKEN)
