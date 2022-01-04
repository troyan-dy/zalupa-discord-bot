from app.cogs.petuh_dialog import PetushDialog
from app.main_bot import MainBot


def main():
    bot = MainBot()

    bot.add_cog(PetushDialog(bot))

    bot.run("OTI3OTY3NTU2NzM0NzAxNjI5.YdR7Ig.vmGqQ9fiIhLxiayZ9ete9hEeWvE")


if __name__ == "__main__":
    main()
