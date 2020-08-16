import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def help(self, ctx):
        embed=discord.Embed()
        embed.set_author(name='Utey Bot help page' ,icon_url='https://cdn.discordapp.com/attachments/744238704914202764/744238756974035064/info.png')   #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        embed.add_field(name='Utility:',value=
        '`help` - you\'re here! More info on my [discord](https://discord.gg/vzVmhFB).\n' +
        '`announce <channel> <role [-n if none]> <message>` - send an announcement.\n' +
        '`ping` - get the bot ping (response time).\n' +
        '`invite` - quickly create an invite link.\n'
        '`info` - some facts and info about Utey.', inline=False)
        embed.add_field(name='Moderation:', value=
        '`ban <user>` - use to ban a user.\n', inline=False)
        embed.add_field(name='Fun:', value=
        '`fact` - fetch a random fact from r/facts.', inline=False)
        
        embed.set_footer(text='For more info message senshi#0001 on discord.')
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        amount = len(ctx.bot.guilds)

        embed=discord.Embed()
        embed.set_author(name='Utey statistics' ,icon_url='https://cdn.discordapp.com/attachments/700737308189523969/743932076256133261/oRNl8yW.png')   
        embed.add_field(name='Servers:',value='Currently I\'m on ' + str(amount) + ' servers.', inline=False)
        embed.add_field(name='Code:',value='[My code](https://github.com/ssenshi/Utey1.2) is and always will remain public.', inline=False)
        embed.set_footer(text='For more info message senshi#0001 on discord.')
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)

    async def ping(self, ctx):

        ping = round(self.bot.latency,1)
        embed=discord.Embed()
        embed.set_author(name='Pong!' ,icon_url='https://cdn.discordapp.com/attachments/700737308189523969/743934244526751935/2333011.png')   
        embed.add_field(name=f'My ping is {ping} seconds',value='Ping is the time it takes the host to communicate with the client.', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
