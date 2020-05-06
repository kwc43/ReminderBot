import discord
from discord.ext import commands

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member:discord.Member):
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')


    @commands.command(name='perms', aliases=['permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member:discord.Member=None):
        if not member:
            member = ctx.author
        
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)

    @commands.command(name='clear', aliases=['purge', 'clean'])
    @commands.has_role('admin')
    async def clear_chat(self, ctx, totalToDelete):
        channel = ctx.channel 
    #wip, need to delete in bulk not one by one, shouldn't delete the command itself
        async for message in channel.history(limit = int(totalToDelete)):
            await message.delete()
        
        response = f'Deleted {totalToDelete} from {ctx.guild.name}'

        await ctx.send(response)
    """
    @commands.command(name='ma', help='Message all users')
    @commands.guildonly()
    async def ma(ctx):
        guild = ctx.guild
        users = guild.members
        for user in users:
            await user.dm_channel.send(
                f'Hi {user.name}'
            )
        response = 'Message has been sent to all users'
        await ctx.send(response)

    @bot.command(name='hello', help='Says hello back')
    async def hello(ctx):
        response = 'hello retard'
        await ctx.send(response)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You are not permitted to use this command.')
        else:
            await ctx.send(error)
    """
def setup(bot):
    bot.add_cog(GeneralCog(bot))