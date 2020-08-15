import discord
from discord.ext import commands

class invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite()
        await ctx.send(link)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(invite(bot))
