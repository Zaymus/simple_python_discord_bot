import discord
from discord.ext import commands
import os

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)#gets ping of the user from the bot and converts it to ms instead of seconds

        #conditioning that changes colour of ping depending on how severe it is ((diff +, fix, diff -) (green = good, yellow = ok, red = bad))
        if(ping <= 80):
            await ctx.send(f':satellite:```diff\n PONG!\n+ {ping}ms```:satellite_orbital:')
        elif(ping <= 150):
            await ctx.send(f':satellite:```fix\nPONG!\n+ {ping}ms```:satellite_orbital:')
        else:
            await ctx.send(f':satellite:```diff\nPONG!\n- {ping}ms```:satellite_orbital:')

    @commands.command()
    async def join(self, ctx, team):
        is_registered = False
        with open("team_list.txt", "r") as file:
                for line in file.readlines():
                    if line == str(team):
                        is_registered = True
                        break


        if is_registered:
            await ctx.send(f'Team {team} has already been registered to this tournament.')

        else:
            with open("team_list.txt", "a") as file:
                file.write(str(team) + "\n")

            await ctx.send(f'Team {team} has been successfully registered to this tournament.\nGood Luck!')

    @commands.command()
    async def clear(self, ctx, team = None):
        if team is None:
            with open("team_list.txt", "w") as file:
                file.truncate()

            await ctx.send("Successfully cleared list of teams")
        else:
            teams = []
            with open("team_list.txt", "a+") as file:
                teams = [line for line in file.readlines() if line.lower() != str(team).lower()]
                file.truncate()
                for t in teams:
                    file.write(str(t) + "\n")

            await ctx.send(f'Successfully removed team {team} from the team list')

    @commands.command()
    async def list(self, ctx):
        file = open("team_list.txt", 'r')

        await ctx.send(f'```{file.read()}```' )

def setup(bot):
    bot.add_cog(Commands(bot))
