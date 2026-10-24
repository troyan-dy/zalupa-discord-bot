import uvloop

from app.cogs.petuh_dialog import PetushDialog
from app.main_bot import MainBot
from app.settings import Settings


async def main():
    settings = Settings()
    async with MainBot() as bot:
        bot.logger.info(f"env: {settings.env}")
        if settings.env == "prod":
            bot.logger.info("include sentry_sdk")
            bot.use_sentry(dsn=str(settings.sentry_dsn))
        await bot.add_cog(PetushDialog(bot))
        bot.logger.info("Подготовка подготовлена")

        await bot.start(settings.bot_token)


if __name__ == "__main__":
    uvloop.run(main())
