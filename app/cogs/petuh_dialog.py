from discord.ext.commands import Cog, Context, command


class PetushDialog(Cog):
    @command("петух", pass_context=True)
    async def petuh(self, ctx: Context, val=None):
        await ctx.send("Каво!!! а может быть ты петух!!! м!!?!?!?")
        if val:
            await ctx.send(f"Хотя действительно, {val} - петух!!")
