import discord
import os
from discord.ext import commands

f = open("C:\\Users\\carso\\Desktop\\discord_token.txt", "r")
token = f.read()

bot = commands.Bot(command_prefix = '.')

#for loop that loads all files within the cogs folder and removes the extension from the string
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')

bot.run(token)
