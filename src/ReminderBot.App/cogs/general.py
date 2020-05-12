import discord
from discord.ext import commands

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joined', help='Shows when a user joined the server')
    @commands.guild_only()
    async def joined(self, ctx, member:discord.Member):
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')


    @commands.command(name='perms', aliases=['permissions'], help='Shows the current users permissions')
    @commands.guild_only()
    async def check_permissions(self, ctx, member:discord.Member=None):
        if not member:
            member = ctx.author
        
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(GeneralCog(bot))