import logging
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime

from discord.ext.commands import Command as _Command
from discord.ext.commands import command as _command

from app.logger import LoggerMixin

start_time = ContextVar("start_time")


standart_logger = logging.getLogger(__name__)


@contextmanager
def logged(key, logger=None):
    if logger is None:
        logger = standart_logger
    start = datetime.utcnow()
    logger.info(f"'{key}' started")
    try:
        yield
    finally:
        logger.info(f"'{key}' finished, spend: {datetime.utcnow() - start}")


class Command(_Command, LoggerMixin):
    async def call_before_hooks(self, ctx):
        start_time.set(datetime.utcnow())
        self.logger.info(f"'{self.name}' started")
        return await super().call_before_hooks(ctx)

    async def call_after_hooks(self, ctx):
        stop = datetime.utcnow()
        self.logger.info(f"'{self.name}' finished, spend: {stop - start_time.get()}")
        return await super().call_after_hooks(ctx)


def command(name, **attrs):
    def decorator(func):
        return Command(func, name=name, **attrs)

    return decorator
