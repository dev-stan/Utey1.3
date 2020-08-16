import discord
from discord.ext import commands

class botinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def about(self, ctx):

        embed=discord.Embed()
        embed.set_author(name='About Utey' ,icon_url='https://cdn.discordapp.com/attachments/700737308189523969/743932076256133261/oRNl8yW.png')   
        embed.add_field(name='Servers:',value='Currently I\'m on ' + str(len(ctx.bot.guilds)) + ' servers.', inline=False)
        embed.add_field(name='Code:',value='[My code](https://github.com/ssenshi/Utey1.2) is right here.', inline=False)
        embed.set_footer(text='For more info message senshi#0001 on discord.')

        await ctx.send(embed=embed)

    
    @commands.command(pass_context=True)
    async def ping(self, ctx):

        ping = round(self.bot.latency,1)
        embed=discord.Embed()
        embed.set_author(name=f'My ping is {ping} seconds.' ,icon_url='https://cdn.discordapp.com/attachments/700737308189523969/743934244526751935/2333011.png')
           
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botinfo(bot))