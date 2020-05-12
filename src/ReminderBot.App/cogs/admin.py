import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TODO - add option to delete only a member's message
    @commands.command(name='clear', aliases=['purge', 'clean'], help='Delete the past x messages, default is 100')
    @commands.has_role('admin')
    async def clear_chat(self, ctx, totalToDelete=100, member:discord.Member=None):
        channel = ctx.channel

        deleted = await channel.purge(limit = totalToDelete)

        await channel.send('Deleted {} message(s)'.format(len(deleted)))

    @commands.command(name='shout', aliases=['message_all', 'ma', ], help='Message all users under a given role')
    @commands.guild_only()
    @commands.has_role('admin')
    async def ma(self, ctx, msg, role='@everyone'):
        users_messaged = []

        for m in ctx.guild.members :
            if (not m.bot 
            and m != ctx.author):
             if any(r.name == role for r in m.roles):
                 #TODO maybe make the messaged prettier, embed?
                await m.send(
                    f'{ctx.author} says: {msg}'
                )
                users_messaged.append(m)

        #TODO maybe make this prettier, embed?
        await ctx.author.send(f'Messaged sent to {users_messaged}')

def setup(bot):
    bot.add_cog(AdminCog(bot))