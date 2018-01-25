from datetime import datetime

def convert_data(data):
	try:
		newShow = data[0]['Headline display text (required)']
	except:
		newShow = 'invalid_data'
	return {
		'createdData': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		'newShow': newShow,
		'rawData': data
	}

