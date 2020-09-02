import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('the market'))
        #prints to console when the bot is ready to be used after initial startup
        print("py bot is online!")

def setup(bot):
    bot.add_cog(Events(bot))
