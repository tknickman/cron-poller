from tinydb import TinyDB, Query


db = TinyDB('/home/tknickman/db/reply_all.json')

def save_data(data):
	return db.insert(data)

def has_changed(last_doc_id):
	doc = db.get(doc_id=last_doc_id)
	doc_1 = db.get(doc_id=last_doc_id - 1)
	if doc_1 is not None:
		return doc['newShow'] != doc_1['newShow']
	else:
		return False

