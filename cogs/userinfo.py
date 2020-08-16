import discord
from discord.ext import commands

class userinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        if not member:
            member = ctx.message.author
        

        embed = discord.Embed()
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name='Display name:', value=member.display_name, inline=False)
        embed.add_field(name='ID:', value=member.id, inline=False)

        embed.add_field(name='Created at: ', value=member.created_at.strftime('%a, %#d, %B, %Y, %I:%M, %p UTC'), inline=False)
        embed.add_field(name='Joined at: ', value=member.joined_at.strftime('%a, %#d, %B, %Y, %I:%M, %p UTC'), inline=False)


        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(userinfo(bot))