import sys

from colorama import init, Fore

from src.utils.username_searcher import searcher
from src.utils.bomber import sms
from src.utils import fake_person, ip, pinger, pcinfo, webhookspam, ddos, phone, discord_server_crash, anti_banword


def main():
	init()
	import os
	clear = lambda: os.system('cls')
	clear()
	ip.log()
	print(Fore.LIGHTRED_EX + r'''

	   ░██████╗██╗░█████╗░░██████╗░███╗░░░███╗░█████╗░
	   ██╔════╝██║██╔══██╗██╔════╝░████╗░████║██╔══██╗
	   ╚█████╗░██║██║░░██║██║░░██╗░██╔████╔██║██║░░██║
	   ░╚═══██╗██║██║░░██║██║░░╚██╗██║╚██╔╝██║██║░░██║
	   ██████╔╝██║╚█████╔╝╚██████╔╝██║░╚═╝░██║╚█████╔╝ ''')
	print(Fore.RESET)

	commands = int(input('\033[1m' + Fore.LIGHTBLACK_EX + '''
	╔════════════════════════════════════════════════════╗
	║''' + Fore.LIGHTRED_EX + '''  [1] - СМС Бомбер           [7] - ДДОС             ''' + Fore.LIGHTBLACK_EX + '''║
	║''' + Fore.LIGHTRED_EX + '''  [2] - Поиск по IP          [8] - Фейк личность    ''' + Fore.LIGHTBLACK_EX + '''║
	║''' + Fore.LIGHTRED_EX + '''  [3] - Поиск по никнейму    [9] - Пинговать IP     ''' + Fore.LIGHTBLACK_EX + '''║
	║''' + Fore.LIGHTRED_EX + '''  [4] - Инфо по номеру       [10] - Вебхук спам     ''' + Fore.LIGHTBLACK_EX + '''║
	║''' + Fore.LIGHTRED_EX + '''  [5] - Анти банворд         [11] - Крашер серверов ''' + Fore.LIGHTBLACK_EX + '''║
	║''' + Fore.LIGHTRED_EX + '''  [6] - Информация о пк      [12] - Выход           ''' + Fore.LIGHTBLACK_EX + f'''║
	╚════════════════════════════════════════════════════╝

	╔════════════════════════════════════════════════════╗
	║''' + Fore.LIGHTRED_EX + '''          tg: @eZTTPkAI    ds: shmyaks.             ''' + Fore.LIGHTBLACK_EX + f'''║
	╚════════════════════════════════════════════════════╝

	  ''' + Fore.LIGHTRED_EX + '''Выберите пункт >>  '''))

	if commands == 1:
		sms.sms_spam()
	elif commands == 2:
		ip.search()
	elif commands == 3:
		searcher.recon()
	elif commands == 4:
		phone.print_number_info()
	elif commands == 5:
		anti_banword.transform_text()
	elif commands == 6:
		pcinfo.getSystemInfo()
	elif commands == 7:
		ddos.ddos()
	elif commands == 8:
		fake_person.fake()
	elif commands == 9:
		pinger.ping()
	elif commands == 10:
		webhookspam.spam()
	elif commands == 11:
		discord_server_crash.crash()
	elif commands == 12:
		sys.exit()
	else:
		main()


if __name__ == "__main__":
	main()
