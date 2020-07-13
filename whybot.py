from asyncio import sleep
import discord
from covid19 import *
from discord.ext import commands
from random import *


bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')
    await bot.change_presense(status = discord.Status.online, activity=discord.Game('Eating some dog'))


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx,amount:int =5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Cleared {amount} message(s)!')
    await sleep(2)
    await ctx.channel.purge(limit=1)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member} for {rason}')

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member} for {rason}')

'''@bot.comamnd()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        '''

@bot.command()
async def covid(ctx):
    embed = discord.Embed(title='Latest covid update', color=3447003)
    embed.add_field(name = get_update_date(), value= get_data_covid())
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()  
async def math(ctx,arg):
    result = eval(arg)
    await ctx.send(result)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))



bot.run('NzIxMTgzNzTOKENTOKENq8vi3HNEvQv9EFQu8')
