from asyncio import sleep
import discord
from covid19 import *
from discord.ext import commands

bot = commands.Bot(command_prefix='=')


@bot.command()
async def covid(ctx):
    embed = discord.Embed(title='Latest covid update')
    embed.add_field(name = get_update_date(), value= get_data_covid())
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def math(ctx,arg):
    result = eval(arg)
    await ctx.send(result)

bot.run('TOKEN')
