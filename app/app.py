from app.cogs.petuh_dialog import PetushDialog
from app.main_bot import MainBot
from app.settings import Settings


def main():
    settings = Settings()
    bot = MainBot()

    bot.add_cog(PetushDialog(bot))

    bot.run(settings.bot_token)


if __name__ == "__main__":
    main()
