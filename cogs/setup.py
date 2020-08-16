import discord
from discord.ext import commands

class start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is up and runnig..')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help | ;inviteme"))

def setup(bot):
    bot.add_cog(start(bot))