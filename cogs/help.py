import discord
from discord.ext import commands
import json
import requests

class helpmsg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed()
        embed.set_author(name='Utey Bot help page' ,icon_url='https://cdn.discordapp.com/attachments/744238704914202764/744238756974035064/info.png')   #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        embed.add_field(name='Utility:',value=
        '`help` - you\'re here! More info on my [discord](https://discord.gg/vzVmhFB).\n' 
        '`announce <channel> <role [-n if none]> <message>` - send an announcement.\n'
        '`poll <question>` - create a poll.\n'
        '`userinfo <member>` - displays basic information about a user.\n'
        '`status` - check the status of discord servers.\n'
        '`mcstatus <ip>` - check if a Minecraft server is online.\n' 
        '`ping` - get the bot ping (response time).\n' 
        '`invite` - quickly create an invite link.\n'
        '`about` - some facts and info about Utey.', inline=False)
        embed.add_field(name='Moderation:', value=
        '`ban <user>` - ban a user.\n', inline=False)
        embed.add_field(name='Fun:', value=
        '`fact` - fetch a random fact from r/facts.\n'
        '`meme` - fetch a random meme from the top of r/memes.\n',inline=False)
        embed.set_footer(text='For more info message senshi#0001 on discord.')
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpmsg(bot))