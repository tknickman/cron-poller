import requests

from settings import mail_gun_config
from helpers import log_error


def send_notification(message, subject):
    return requests.post(
        mail_gun_config['host'],
        auth=("api", mail_gun_config['api_key']),
        data={
      	  "from": mail_gun_config['from'],
      	  "to": "Thomas Knickman <tknickman@gmail.com>",
      	  "subject": subject,
      	  "text": message
      	 }
  	 )


def send_message(message, subject):
	try: 
		send_notification(message, subject)
	except Exception as e:
		log_error(e)


