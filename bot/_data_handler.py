from discord.ext import tasks, commands
from replit import db
import os
import json
from logger import get_logger

class DataHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = get_logger()
        cur_path = os.path.dirname(__file__)
        self.backup = os.path.relpath('..\\backup.json', cur_path)
        self.save_data.start()

    def cog_unload(self):
        self.save_data.cancel()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')
        self.logger.info(f'{self.bot.user.name} has connected to Discord!')

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
            author_data = dict(gathering['author'])
            gathering_data['author'] = author_data
            users_data = [dict(user) for user in list(gathering['users'])]
            gathering_data['users'] = users_data
            data.append(gathering_data)

        with open(self.backup, 'w') as file:
            json.dump(data, file)
