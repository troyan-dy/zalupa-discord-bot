import asyncio
import random
import ssl

import aiohttp
import certifi
from discord.ext.commands import Bot

from app.health_check import health_check as health_check


class MainBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(
            connector=aiohttp.TCPConnector(
                ssl=ssl.create_default_context(
                    cafile=certifi.where(),
                ),
            ),
            command_prefix="!",
            *args,
            **kwargs
        )

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")
        asyncio.create_task(health_check)
