import main
import requests


def print_number_info():
	user_number = input("Введите номер телефона (например, +79833170773): ").strip()

	if user_number:
		print("Поиск данных...\n")
		info = requests.get(
			f'https://htmlweb.ru/geo/api.php?json&telcod={user_number}')
		data = info.json()

		if data.get("status_error"):
			print("Ошибка: Не удалось получить данные. Проверьте номер телефона и попробуйте снова.")
			return

		if data.get("limit") == 0:
			print("Вы израсходовали все лимиты запросов.")
			return

		country = data.get('country', {})
		region = data.get('region', {})
		other = data.get('0', {})

		print(f"Страна: {country.get('name', 'Не найдено')}, {country.get('fullname', 'Не найдено')}")
		print(f"Город: {other.get('name', 'Не найдено')}")
		print(f"Почтовый индекс: {other.get('post', 'Не найдено')}")
		print(f"Код валюты: {country.get('iso', 'Не найдено')}")
		print(f"Телефонные коды: {data.get('capital', {}).get('telcod', 'Не найдено')}")
		print(f"Посмотреть в wiki: {other.get('wiki', 'Не найдено')}")
		print(f"Гос. номер региона авто: {region.get('autocod', 'Не найдено')}")
		print(f"Оператор: {other.get('oper', 'Не найдено')}, {other.get('oper_brand', 'Не найдено')}, {other.get('def', 'Не найдено')}")
		print(f"Местоположение: {country.get('name', 'Не найдено')}, {region.get('name', 'Не найдено')}, {other.get('name', 'Не найдено')} ({region.get('okrug', 'Не найдено')})")

		latitude = other.get('latitude', 'Не найдено')
		longitude = other.get('longitude', 'Не найдено')
		location = data.get('location', 'Не найдено')
		lang = country.get('lang', 'Не найдено').title()
		lang_code = country.get('langcod', 'Не найдено')
		capital = data.get('capital', {}).get('name', 'Не найдено')

		print(f"Открыть на карте (google): https://www.google.com/maps/place/{latitude}+{longitude}")
		print(f"Локация: {location}")
		print(f"Язык общения: {lang}, {lang_code}")
		print(f"Край/Округ/Область: {region.get('name', 'Не найдено')}, {region.get('okrug', 'Не найдено')}")
		print(f"Столица: {capital}")
		print(f"Широта/Долгота: {latitude}, {longitude}")
		print(f"Оценка номера в сети: https://phoneradar.ru/phone/{user_number}")

	else:
		print("Ошибка: Номер телефона не введен.")


	input('\nНажмите Enter для возврата в главное меню')
	main.main()
