from discord.ext import commands
from copy import deepcopy
from replit import db

# Models
from models import Topics, Gathering

# Util
import util

# Cogs
import bot._tasks as _tasks


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
            await ctx.send(
                '\n'.join([gathering.toString() for gathering in gatherings])
            )

    async def select_topics(self, ctx, length):
        def check(msg):
            if (msg.author == ctx.author) and (msg.channel == ctx.channel):
                return True
            else:
                return False

        available_topics = Topics(deepcopy(Topics.all_topics))
        result_list = []
        while len(result_list) < length:
            await ctx.send(
                'Type the number corresponding to the topic to select it:\n{0}'
                .format(available_topics.pprint())
            )
            msg = await self.wait_for('message', check=check)
            index = util.str_to_int(msg.content)
            if index > len(available_topics) - 1:
                raise ValueError(
                    "Your selection must be between 1 and {0}".
                    format(len(available_topics) - 1)
                )
            result_list.append(available_topics[index])
            available_topics.remove(index)
        await ctx.send(f'Your selections are: {", ".join(result_list)}')
        return result_list

    def pprint_gatherings(self, gatherings):
        gatherings_dict = {
            i: gatherings[i] for i in range(0, len(gatherings))
        }

        return '\n'.join([
            "{0}: {1}".format(key, gathering)
            for key, gathering in gatherings_dict.items()
        ])


# Export:
scheduling_bot = Bot()
scheduling_bot.add_cog(_tasks.TasksCog())
