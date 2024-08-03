from colorama import Fore

import main

import faker


def fake():
	faki = faker.Faker('ru_RU')
	print(Fore.LIGHTRED_EX + '\033[1m' + 'ФИО: ' + faki.name())
	print(Fore.LIGHTRED_EX + '\033[1m' + 'Страна: ' + faki.current_country())
	print(Fore.LIGHTRED_EX + '\033[1m' + 'Адрес: ' + faki.address())
	print(Fore.LIGHTRED_EX + '\033[1m' + 'Номер телефона: ' + faki.phone_number())
	print(Fore.LIGHTRED_EX + '\033[1m' + 'Почта: ' + faki.email())

	input('\nНажмите Enter для возврата в главное меню')
	main.main()
