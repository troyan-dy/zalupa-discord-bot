import ssl

import aiohttp
import certifi
from discord.ext.commands import Bot, Context

from app.logger import LoggerMixin


class MainBot(Bot, LoggerMixin):
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
        self.logger.info("Logged in as")
        self.logger.info(self.user.name)
        self.logger.info(self.user.id)
        self.logger.info("------")

    async def on_command_error(self, ctx: Context, error: Exception):
        raise Exception from error
