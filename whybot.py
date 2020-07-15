from asyncio import sleep
import discord
from discord.ext import commands
import random
from covid19 import * 


bot = commands.Bot(command_prefix='=')
bot.remove_command('help')



@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('-------------')
	await bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Baby shark ,=help"))

@bot.event
async def on_member_join(member):
	print("Recognised that a member called " + member.name + " joined")
	welcome_message = random.choice(['We hope you bring pizza','Have fun here!'])
	guild = discord.utils.get(member.guild.name)
	print(guild)
	channel = discord.utils.get(member.guild.channels, name = "welcome")
	await channel.send(f"Welcome {member.mention} to Coolest lab in the world , whydude's lab!!! {welcome_message}")

####verify and role selecting
@bot.event
async def on_raw_reaction_add(payload):
	global role

	message_id = payload.message_id
	if message_id == 732906155969478716:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

		role = None

		if payload.emoji.name == 'verify':
			role = discord.utils.get(guild.roles, name='Verified ✔')

		if role is not None:
			print(role.name)
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
			if member is not None:
				await member.add_roles(role)
				print(f'Gave {role} role to {member}')
			else:
				print('No member')

	if message_id == 732849702055444520:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

		role = None

		if payload.emoji.name == 'python':
			role = discord.utils.get(guild.roles, name='Python')

		elif payload.emoji.name == 'javascript':
			role = discord.utils.get(guild.roles, name='Javascript')

		elif payload.emoji.name == 'male':
			role = discord.utils.get(guild.roles, name='He')

		elif payload.emoji.name == 'female':
			role = discord.utils.get(guild.roles, name='She')

		elif payload.emoji.name == 'windows':
			role = discord.utils.get(guild.roles, name='Windows')

		elif payload.emoji.name == 'linux':
			role = discord.utils.get(guild.roles, name='Linux')

		elif payload.emoji.name == 'mac':
			role = discord.utils.get(guild.roles, name='Mac')

		elif payload.emoji.name == 'DJ':
			role = discord.utils.get(guild.roles, name='DJ')

		elif payload.emoji.name == 'android':
			role = discord.utils.get(guild.roles, name='Android')

		elif payload.emoji.name == 'ios':
			role = discord.utils.get(guild.roles, name='IOS')

		elif payload.emoji.name == 'sk':
			role = discord.utils.get(guild.roles, name='Suankularb')



		if role is not None:
			print(role.name)
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
			if member is not None:
				await member.add_roles(role)
				print(f'Gave {role} role to {member}')
			else:
				print('No member')
####
@bot.event
async def on_raw_reaction_remove(payload):
	global role

	message_id = payload.message_id
	if message_id == 732906155969478716:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

		role = None

		if payload.emoji.name == 'verify':
			role = discord.utils.get(guild.roles, name='Verified ✔')

		if role is not None:
			print(role.name)
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
			if member is not None:
				await member.remove_roles(role)
				print(f'Removed {role} role of {member}')
			else:
				print('No member')

	if message_id == 732849702055444520:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

		role = None

		if payload.emoji.name == 'python':
			role = discord.utils.get(guild.roles, name='Python')

		elif payload.emoji.name == 'javascript':
			role = discord.utils.get(guild.roles, name='Javascript')

		elif payload.emoji.name == 'male':
			role = discord.utils.get(guild.roles, name='He')

		elif payload.emoji.name == 'female':
			role = discord.utils.get(guild.roles, name='She')

		elif payload.emoji.name == 'windows':
			role = discord.utils.get(guild.roles, name='Windows')

		elif payload.emoji.name == 'linux':
			role = discord.utils.get(guild.roles, name='Linux')

		elif payload.emoji.name == 'mac':
			role = discord.utils.get(guild.roles, name='Mac')

		elif payload.emoji.name == 'DJ':
			role = discord.utils.get(guild.roles, name='DJ')

		elif payload.emoji.name == 'android':
			role = discord.utils.get(guild.roles, name='Android')

		elif payload.emoji.name == 'ios':
			role = discord.utils.get(guild.roles, name='IOS')

		elif payload.emoji.name == 'sk':
			role = discord.utils.get(guild.roles, name='Suankularb')



		if role is not None:
			print(role.name)
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
			if member is not None:
				await member.remove_roles(role)
				print(f'Remove {role} role of {member}')
			else:
				print('No member')

@bot.command()
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.orange()
	)

	embed.set_author(name='Help')
	embed.add_field(name='Prefix', value='=')
	embed.add_field(name='covid [2 letter country code]', value='Give you latest covid 19 data of specific country', inline=False)
	embed.add_field(name='covidglobal', value= 'Give you latest covid 19 worldwide', inline=False)
	embed.add_field(name='clear [int]', value= 'Purge previous [int] message', inline=False)
	embed.add_field(name='kick [@member,reason]', value= 'Kick @member for [reason]', inline=False)
	embed.add_field(name='ban [@member,reason]', value= 'Ban @member for [reason]', inline=False)
	embed.add_field(name='math [2+3**89+5*6]', value= 'Fast calculator', inline=False)
	embed.add_field(name='joined [@member]', value= 'Tell when @member joined', inline=False)

	await author.send(author, embed=embed)

@bot.command()
async def covid(ctx,arg):
    arg = arg.upper()
    embed = discord.Embed(title=f'Latest {arg} covid update', color=3447003)
    embed.add_field(name = get_update_date(arg), value= get_data_covid(arg))
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def covidglobal(ctx):
    embed = discord.Embed(title='Latest worldwide covid update', color=3447003)
    embed.add_field(name = 'Update date unavaliable', value= get_data_wovid())
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx,amount:int =5):
	await ctx.channel.purge(limit=amount+1)
	await ctx.send(f'Cleared {amount} message(s)!')
	await sleep(2)
	await ctx.channel.purge(limit=1)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member} for {reason}')

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member} for {reason}')

@bot.command()  
async def math(ctx,arg):
	result = eval(arg)
	await ctx.send(result)

@bot.command()
async def joined(ctx, member: discord.Member):
	"""Says when a member joined."""
	await ctx.send(f'{member.name} joined in {member.joined_at}')





bot.run('NzIxMTgzNzY5MTI1NTg0OTI5.Xw6AKA.F9ldm4jkyxLxa5Q1EIrjGDQxeYY')
