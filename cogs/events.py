import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.Cog.listener()
    async def on_ready(self):
        #prints to console when the bot is ready to be used after initial startup
        print("py bot is online!")

def setup(bot):
    bot.add_cog(Events(bot))
