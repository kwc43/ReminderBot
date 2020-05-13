import discord
import random
from discord.ext import commands

class RngCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', aliases=['r'])
    @commands.guild_only()
    async def roll(self, ctx, roll:str='1d20'):
        result = []

        try:
            #TODO limit timesToRoll? 
            timesToRoll, diceType = map(int, roll.split('d'))
        except Exception as e:
            #TODO Should log it instead
            print(e)
            await ctx.send(f'{ctx.message.author.name}, Invalid format must be in xdy!')

        #TODO implement better random
        result = [random.randint(1, diceType) for i in range(timesToRoll)]

        #should probably print it in a prettier format
        await ctx.send(ctx.message.author.mention + f":game_die:\n **Result**({roll}): {result} \n**Total**: {sum(result)}" )



def setup(bot):
    bot.add_cog(RngCog(bot))