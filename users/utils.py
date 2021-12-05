import uuid #universal  unique identifier

def get_random_code(self):
	code = str(uuid,uuid4())[:8].replace('-','').lower()
	return code