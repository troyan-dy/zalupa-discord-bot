import asyncio
import random

from discord.ext.commands import Context
from discord.ext.tasks import loop

from app.cogs.base import BaseCog
from app.commands import command

MIN_PENIS_LEN = 3
MAX_PENIS_LEN = 14


class PetushDialog(BaseCog):
    @command("петух")
    async def petuh(self, ctx: Context):
        await ctx.send(f"Каво!!! а может быть ты(<@{self.author_id(ctx)}>) петух!!! м!!?!?!?")

    @command("пенис")
    async def penis_len(self, ctx: Context):
        author_id = self.author_id(ctx)
        length = random.randint(MIN_PENIS_LEN, MAX_PENIS_LEN)
        await ctx.send(f"У <@{author_id}> гиганская пенисина, целых {length}см")

    # Отключено: для включения вызвать self.ping_say.start() при инициализации cog
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
