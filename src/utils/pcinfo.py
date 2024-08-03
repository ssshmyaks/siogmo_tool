import platform, socket, re, uuid, psutil, logging
from colorama import Fore

import main


def getSystemInfo():
	try:
		info = {}
		info['platform'] = platform.system()
		info['platform-release'] = platform.release()
		info['architecture'] = platform.machine()
		info['hostname'] = socket.gethostname()
		info['ip-address'] = socket.gethostbyname(socket.gethostname())
		info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		info['processor'] = platform.processor()
		info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"

		info = '\033[1m' + Fore.LIGHTRED_EX + f"""
		ОС: {info['platform']}
		Версия ОС: {info['platform-release']}
		Архитектура: {info['architecture']}
		Имя: {info['hostname']}
		IP: {info['ip-address']}
		MAC: {info['mac-address']}
		Процессор: {info['processor']}
		Оперативная память: {info['ram']}
		"""
		print(info)
		input('\nНажмите Enter для возврата в главное меню')
		main.main()
	except Exception as e:
		logging.exception(e)
