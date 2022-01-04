from app.logger import LoggerMixin
from discord.ext.commands import Bot, Cog, Context


class BaseCog(Cog, LoggerMixin):
    def __init__(self, bot: Bot):
        self.bot = bot

    def author_id(self, ctx: Context) -> int:
        return ctx.message.author.id
