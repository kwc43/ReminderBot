import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TODO - need to delete in bulk not one by one, shouldn't delete the command itself
    @commands.command(name='clear', aliases=['purge', 'clean'], help='Delete the past x messages')
    @commands.has_role('admin')
    async def clear_chat(self, ctx, totalToDelete):
        channel = ctx.channel 
        async for message in channel.history(limit = int(totalToDelete)):
            await message.delete()
        
        response = f'Deleted {totalToDelete} from {ctx.guild.name}'

        await ctx.send(response)
    
    #TODO - make role optional, default to all if no role given, shouldn't send message to user that invoked the command
    @commands.command(name='ma', aliases=['message_all', 'shout'], help='Message all users under a given role')
    @commands.guild_only()
    @commands.has_role('admin')
    async def ma(self, ctx, role, msg):
        for m in ctx.guild.members :
            if not m.bot and any(r.name == role for r in m.roles):
                await m.send(
                    f'{msg}'
                )

def setup(bot):
    bot.add_cog(AdminCog(bot))