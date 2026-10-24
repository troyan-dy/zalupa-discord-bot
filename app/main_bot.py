import ssl

import aiohttp
import certifi
import discord
import sentry_sdk
from discord.ext.commands import Bot, Context

from app.logger import LoggerMixin


class MainBot(Bot, LoggerMixin):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            *args,
            connector=aiohttp.TCPConnector(
                ssl=ssl.create_default_context(
                    cafile=certifi.where(),
                ),
            ),
            command_prefix="!",
            intents=intents,
            **kwargs,
        )

    def use_sentry(self, **sentry_args):
        sentry_sdk.init(**sentry_args)

    async def on_ready(self):
        self.logger.info("Logged in as")
        self.logger.info(self.user.name)
        self.logger.info(self.user.id)
        self.logger.info("------")

    async def on_error(self, event_method: str, *args, **kwargs):
        sentry_sdk.capture_exception()
        await super().on_error(event_method, *args, **kwargs)

    async def on_command_error(self, ctx: Context, error: Exception):
        raise Exception from error
