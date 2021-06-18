from discord.ext import tasks, commands
from datetime import datetime
from replit import db


class CleanupCog(commands.Cog):

    @tasks.loop(minutes=5.0)
    async def cleanup(self):
        try:
            for gathering_data in db['gatherings']:
                start_time = datetime.strptime(
                    gathering_data['date_time'], '%m-%d-%Y %H:%M'
                )
                if start_time < datetime.now():
                    db['gatherings'].remove(gathering_data)
        except Exception as e:
            print(str(e))
