import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        if(ping <= 80):
            await ctx.send(f':satellite:```diff\n PONG!\n+ {ping}ms```:satellite_orbital:')
        elif(ping <= 150):
            await ctx.send(f':satellite:```fix\nPONG!\n+ {ping}ms```:satellite_orbital:')
        else:
            await ctx.send(f':satellite:```diff\nPONG!\n- {ping}ms```:satellite_orbital:')

def setup(bot):
    bot.add_cog(Commands(bot))
