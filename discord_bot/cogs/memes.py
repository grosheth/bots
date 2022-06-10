from discord.ext import commands
from random import randint
import discord, aiohttp
from utils import get_mom_joke, get_quote

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!memes get fuckt")
    async def memes(self, ctx):
        memes = {
                1:"https://www.pornhub.com/categories/hentai",
                2:"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                3:"https://www.youtube.com/watch?v=jDwVkXVHIqg",
                4:"https://www.youtube.com/watch?v=N6hVmn9FM7o",
                5: "https://www.youtube.com/watch?v=zNtr0RahRqM"
            }
        
        await ctx.send(memes[randint(1, len(memes))])

    @commands.command(brief="!insult get fuckt")
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_mom_joke()
        await ctx.send(f"{member.display_name} {insult}")

    @commands.command(brief="!quote")
    async def quote(self, ctx):
        quote = await get_quote()
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://picsum.photos/750/500") as r:
                    embed = discord.Embed(title=quote)
                    embed.set_image(url=r._real_url)
                    await ctx.send(embed=embed)
                    

def setup(bot):
    bot.add_cog(Memes(bot))