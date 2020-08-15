import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=';')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzQzOTc0NzI2NTMxMjg1MDYy.XzcedQ.ScRCfiL6aUu9bCBcEEZ43dfAH2o')