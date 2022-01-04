from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command("петух", pass_context=True)
async def add(ctx):
    print(ctx.__dir__)
    await bot.say("Игорь петух")


bot.run("token")
