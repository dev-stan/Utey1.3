import discord
from discord.ext import commands

class embedmsg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def announce(self, ctx, chnl, tag, topic, *, msg):

        channel = ctx.channel.id = chnl[2:-1]
        author = ctx.message.author

        embed=discord.Embed()
        embed.set_author(name=ctx.guild ,icon_url=ctx.guild.icon_url)   
        embed.add_field(name=topic,value=msg, inline=False)
        embed.set_footer(text='For more info message ' + str(author)[:-5] + ' or one of the staff members here on discord.')

        await ctx.send(embed=embed)

        if tag == '-n':
            pass
        elif tag != '-n':
            await ctx.send(tag)
    
    @commands.command()
    async def poll(self, ctx, *, question):

        embed=discord.Embed()
        embed.set_author(name=question)
        embed.set_footer(text=f'Poll created by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('🤷')

def setup(bot):
    bot.add_cog(embedmsg(bot))
