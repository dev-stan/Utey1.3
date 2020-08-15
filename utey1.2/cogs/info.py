import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def info(self, ctx):
        embed=discord.Embed()
        embed.set_author(name='Utey statistics' ,icon_url='https://cdn.discordapp.com/attachments/700737308189523969/743932076256133261/oRNl8yW.png')   
        embed.add_field(name='Servers:',value=len(self.bot.guilds), inline=False)
        embed.set_footer(text='For more info message senshi#0001 on discord.')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))