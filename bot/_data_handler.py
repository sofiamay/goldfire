from discord.ext import tasks, commands
from replit import db
import os
import json

class DataHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        cur_path = os.path.dirname(__file__)
        self.backup = os.path.relpath('..\\backup.json', cur_path)
        self.save_data.start()

    def cog_unload(self):
        self.save_data.cancel()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')

        # Load database from backup
        if 'gatherings' not in db:
            with open(self.backup, 'w') as file:
                db['gatherings'] = json.load(file)

    @tasks.loop(hours=5.0)
    async def save_data(self):
        gatherings = list(db['gatherings'])
        data = []
        for gathering in gatherings:
            gathering_data = dict(gathering)
            gathering_data['topics'] = list(gathering['topics'])
            gathering_data['users'] = list(gathering['users'])
            data.append(gathering_data)

        with open(self.backup, 'w') as file:
            json.dump(data, file)
