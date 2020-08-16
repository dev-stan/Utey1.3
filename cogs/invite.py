
import discord
from discord.ext import commands

class invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):

        link = await ctx.channel.create_invite()

        await ctx.send(link)
        await ctx.message.delete()
    
    @commands.command()
    async def inviteme(self, ctx):

        embed=discord.Embed()
        embed.add_field(name='How to:', value='Simply head [here](https://discord.com/oauth2/authorize?client_id=743912886119694336&permissions=130542679&scope=bot) and complete the easy peasy captcha, thanks for inviting me!')
        
        msg = await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(invite(bot))