from api import get_page
from transform import convert_data
from db import save_data, has_changed
from mail import send_message


supported_pages = [1];

def main():
	for page in supported_pages:
		page_data = get_page(page)
		transformed_data = convert_data(page_data)
		new_doc_id = save_data(transformed_data)

		if (has_changed(new_doc_id)):
			send_message(
				message='Yea pretty much just that, it changed. Sweet bot bro.',
				subject='TEK Bot: Reply All Document Changed'
			)

main()

