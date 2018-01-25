import requests
from settings import api_url_config
from helpers import log_error


def get(url):
	try:
		raw = requests.get(url)
		return raw.json()
	except Exception as e:
		log_error(e)
		return False

def get_page_1():
	return get(api_url_config['replyall_sheet1'])

def get_page_2():
	return get(api_url_config['replyall_sheet2'])

def get_page(sheet=1):
	if sheet == 1:
		return get_page_1()
	elif sheet == 2:
		return get_page_2()
	else:
		return False

