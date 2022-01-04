import sentry_sdk

from app.cogs.petuh_dialog import PetushDialog
from app.main_bot import MainBot
from app.settings import Settings


def main():
    settings = Settings()
    if settings.env == "prod":
        sentry_sdk.init(dsn=settings.sentry_dsn)
    bot = MainBot()
    bot.add_cog(PetushDialog(bot))
    bot.logger.info("Подготовка подготовлена")

    bot.run(settings.bot_token)


if __name__ == "__main__":
    main()
