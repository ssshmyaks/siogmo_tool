import time
import requests
from colorama import Fore
import main


def spam():
	msg = input(Fore.LIGHTRED_EX + '\033[1m' + "\nСообщение для спама: ")
	webhook = input(Fore.LIGHTRED_EX + '\033[1m' + "Вебхук: ")
	times = input(Fore.LIGHTRED_EX + '\033[1m' + "Количество сообщений: ")
	for i in range(int(times)):
		try:
			data = requests.post(webhook, json={'content': msg})
			if data.status_code == 204:
				print(Fore.LIGHTRED_EX + '\033[1m' + "Сообщение отправлено")
		except:
			print(Fore.LIGHTRED_EX + '\033[1m' + "Неправильный вебхук: " + webhook)
			time.sleep(5)
			main.main()
	print(Fore.LIGHTRED_EX + '\033[1m' + "Отправка сообщений закончена")
	time.sleep(5)
	main.main()
