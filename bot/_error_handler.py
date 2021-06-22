import discord
import traceback
import os
from discord.ext import commands
import logging
from logging.handlers import RotatingFileHandler

class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised
        while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers
        # being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten
        # cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions
        # raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception
        # passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(
                    f'{ctx.command} can not be used in Private Messages.'
                )
            except discord.HTTPException:
                pass
        else:
            # All other Errors not returned come here.
            # And we can just print the default TraceBack.
            cur_path = os.path.dirname(__file__)
            log_path = os.path.relpath('..\\err.log', cur_path)
            logger = logging.getLogger("Rotating Log")
            logger.setLevel(logging.ERROR)
            handler = RotatingFileHandler(
                log_path, maxBytes=10000, backupCount=5
            )
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            err_string = ''.join(
                traceback.format_exception(
                    type(error), error, error.__traceback__
                )
            )
            logger.error(err_string)
