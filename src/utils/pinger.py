import socket
from colorama import init, Fore
import time
import main

init()


def tcpping(ip, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		sock.connect((ip, port))
		print(Fore.LIGHTRED_EX + '\033[1m' + f"Подключено к IP {ip}")
		print(Fore.LIGHTRED_EX + '\033[1m' + "Пингую...")
	except:
		print(Fore.LIGHTRED_EX + '\033[1m' + "Произошла ошибка подключения к IP")


def ping():
	ip = input(Fore.LIGHTRED_EX + '\033[1m' + "\nВведите IP: ")
	port = input(Fore.LIGHTRED_EX + '\033[1m' + "Введите порт: ")
	while True:
		try:
			tcpping(ip, int(port))
			time.sleep(0.01)
		except KeyboardInterrupt:
			time.sleep(3)
			main.main()
