import logging
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import UTC, datetime

from discord.ext.commands import Command as _Command

from app.logger import LoggerMixin

start_time: ContextVar[datetime] = ContextVar("start_time")


standart_logger = logging.getLogger(__name__)


@contextmanager
def logged(key, logger=None):
    if logger is None:
        logger = standart_logger
    start = datetime.now(UTC)
    logger.info(f"'{key}' started")
    try:
        yield
    finally:
        logger.info(f"'{key}' finished, spend: {datetime.now(UTC) - start}")


class Command(_Command, LoggerMixin):
    async def call_before_hooks(self, ctx):
        start_time.set(datetime.now(UTC))
        self.logger.info(f"'{self.name}' started")
        return await super().call_before_hooks(ctx)

    async def call_after_hooks(self, ctx):
        stop = datetime.now(UTC)
        self.logger.info(f"'{self.name}' finished, spend: {stop - start_time.get()}")
        return await super().call_after_hooks(ctx)


def command(name, **attrs):
    def decorator(func):
        return Command(func, name=name, **attrs)

    return decorator
