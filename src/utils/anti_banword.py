from colorama import Fore
import main


def transform_text():
	text = input(Fore.LIGHTRED_EX + 'Введите текст:  ')
	translit_dict = {
		'а': '@',
		'б': 'Б',
		'в': 'B',
		'г': 'г',
		'д': 'д',
		'е': 'е',
		'ё': 'ё',
		'ж': 'ж',
		'з': '3',
		'и': 'u',
		'й': 'й',
		'к': 'K',
		'л': 'л',
		'м': 'M',
		'н': 'H',
		'о': '0',
		'п': 'п',
		'р': 'P',
		'с': 'c',
		'т': 'T',
		'у': 'y',
		'ф': 'ф',
		'х': 'X',
		'ц': 'ц',
		'ч': '4',
		'ш': 'ш',
		'щ': 'щ',
		'ъ': 'ъ',
		'ы': 'ы',
		'ь': 'ь',
		'э': 'э',
		'ю': 'ю',
		'я': 'я'
	}

	transformed_text = []

	for char in text:
		if char in translit_dict:
			transformed_text.append(translit_dict[char])
		else:
			transformed_text.append(char)

	print(''.join(transformed_text))
	input('\nНажмите Enter для возврата в главное меню')
	main.main()
