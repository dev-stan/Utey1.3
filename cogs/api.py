import discord
from discord.ext import commands
import requests
import json
import praw
import random


class api(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mcstatus(self, ctx, adress):
        
        response = requests.get(f'https://api.mcsrvstat.us/2/{adress}')
        status = response.content.decode("utf-8")
        status = json.loads(status)

        embed=discord.Embed()
        embed.set_author(name=adress ,icon_url='https://cdn.discordapp.com/attachments/744238704914202764/744681661169664050/minecraft-creeper-face.png')   
        embed.add_field(name='IP:',value=status['ip'], inline=False)
        embed.add_field(name='Port:',value=status['port'], inline=False)
        embed.add_field(name='Version:',value=status['version'], inline=False)
        embed.add_field(name='Online players:',value=status['players']['online'], inline=False)

        await ctx.send(embed=embed)
	
    @commands.command()
    async def status(self, ctx):
        
        response = requests.get('https://srhpyqt94yxb.statuspage.io/api/v2/summary.json')
        status = response.content.decode("utf-8")
        status = json.loads(status)

        embed=discord.Embed()
        embed.set_author(name='Discord server status.' ,icon_url='https://cdn.discordapp.com/attachments/744238704914202764/744321845045493840/discord-512.png')   
        embed.add_field(name='Summary:',value=status['status']['description'], inline=False)
        embed.add_field(name='Indicator: ',value=status['status']['indicator'], inline=False)
        embed.add_field(name='Updated at: ',value=status['page']['updated_at'], inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def fact(self, ctx):

        reddit = praw.Reddit(client_id='a9ZOXTtVzT41cw',
                     client_secret='FPl7Zyvnrj_AzsUMPhl76ZHGuvc',
                     user_agent='pc:utey:1.2 (by u/medievalvanilla)')

        facts_submissions = reddit.subreddit('facts').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in facts_submissions if not x.stickied)

        content = submission.selftext
        title = submission.title
        url = submission.url

        embed=discord.Embed()
        embed.set_author(name='A random fact from r/facts' ,icon_url='https://cdn.discordapp.com/attachments/744238704914202764/744341399914152057/social-36-512.png')   
        embed.add_field(name=title,value=content, inline=False)
        
        try:
            await ctx.send(embed=embed)

        except:
            await ctx.send('Post is too long, try again with `;fact` :negative_squared_cross_mark:')
    
    @commands.command()
    async def meme(self, ctx):

        reddit = praw.Reddit(client_id='a9ZOXTtVzT41cw',
                     client_secret='FPl7Zyvnrj_AzsUMPhl76ZHGuvc',
                     user_agent='pc:utey:1.2 (by u/medievalvanilla)')

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 150)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed()
        embed.set_image(url=submission.url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(api(bot))