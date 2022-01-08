import asyncio
import random

from app.cogs.base import BaseCog
from app.utils import command
from discord.ext.commands import Bot, Context
from discord.ext.tasks import loop


class PetushDialog(BaseCog):
    def __init__(self, bot: Bot):
        super().__init__(bot)
        # self.ping_say.start()

    @command("петух")
    async def petuh(self, ctx: Context):
        await ctx.send(f"Каво!!! а может быть ты(<@{self.author_id(ctx)}>) петух!!! м!!?!?!?")

    @command("пенис")
    async def penis_len(self, ctx: Context):
        await ctx.send(f"У <@{self.author_id(ctx)}> гиганская пенисина, целых {random.randint(3, 14)}см")

    @loop(hours=3)
    async def ping_say(self):
        await self.bot.wait_until_ready()
        text_channel_list = []
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        if text_channel_list:
            await asyncio.gather(*[tc.send("как покакали ребятки?") for tc in text_channel_list])

    @command("error")
    async def some_error(self, ctx: Context):
        raise Exception("test error")
