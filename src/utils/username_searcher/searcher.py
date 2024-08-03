import requests

from colorama import init, Fore

import main
from src.utils.username_searcher.html_urls import header


def recon():
	init()
	print(Fore.LIGHTGREEN_EX + 'Автор: @thelinuxchoice\nАдаптировал: @eZTTPkAI\n')

	username = input('\nВведите никнейм: ')
	print('')

	# vk.com

	formatted_url = 'https://vk.com/' + username
	try:
		r = requests.get(formatted_url)
		r.raise_for_status()
		if r.text != header['vk']:
			print(Fore.LIGHTGREEN_EX + 'Пользователь найден: ' + formatted_url)
	except Exception as e:
		print(Fore.LIGHTRED_EX + 'Пользователь не найден: ' + formatted_url)

	# youtube.com

	formatted_url = 'https://www.youtube.com/@' + username
	try:
		r = requests.get(formatted_url)
		r.raise_for_status()
		if r.text != header['yt']:
			print(Fore.LIGHTGREEN_EX + 'Пользователь найден: ' + formatted_url)
	except Exception as e:
		print(Fore.LIGHTRED_EX + 'Пользователь не найден: ' + formatted_url)

	# github.com

	formatted_url = 'https://www.github.com/' + username
	try:
		r = requests.get(formatted_url)
		r.raise_for_status()
		if r.text != header['gh']:
			print(Fore.LIGHTGREEN_EX + 'Пользователь найден: ' + formatted_url)
	except Exception as e:
		print(Fore.LIGHTRED_EX + 'Пользователь не найден: ' + formatted_url)

	# steam.com

	formatted_url = 'https://steamcommunity.com/id/' + username
	try:
		r = requests.get(formatted_url)
		r.raise_for_status()
		if r.text != header['st']:
			print(Fore.LIGHTYELLOW_EX + 'Пользователь ? найден: ' + formatted_url)
	except Exception as e:
		print(Fore.LIGHTRED_EX + 'Пользователь не найден: ' + formatted_url)

	# t.me

	formatted_url = 'https://t.me/' + username
	try:
		r = requests.get(formatted_url)
		r.raise_for_status()
		if r.text != header['tg']:
			print(Fore.LIGHTYELLOW_EX + 'Пользователь ? найден: ' + formatted_url)
	except Exception as e:
		print(Fore.LIGHTRED_EX + 'Пользователь не найден: ' + formatted_url)

	input('\nНажмите Enter для возврата в главное меню')
	main.main()
