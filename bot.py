import discord
import os
from discord.ext import commands

f = open("C:\\Users\\carso\\Desktop\\discord_token.txt", "r")
token = f.read()#loads bot token that is stored locally on my desktop in a txt file

bot = commands.Bot(command_prefix = '.')# initiallizes bot object with a . prefix for all commands

#for loop that loads all files within the cogs folder and removes the extension from the string
for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')

bot.run(token)#runs the bot using the token that was read from the txt file
