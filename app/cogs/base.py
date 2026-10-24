from discord.ext.commands import Bot, Cog, Context

from app.logger import LoggerMixin


class BaseCog(Cog, LoggerMixin):
    def __init__(self, bot: Bot):
        self.bot = bot

    def author_id(self, ctx: Context) -> int:
        return ctx.message.author.id

    async def cog_command_error(self, ctx, error):
        raise Exception from error
