import hashlib
import bleach

def hash(string):
	"""Returns a SHA224 hash of a string, in a hex-dump string format."""
	return hashlib.sha224(string.encode()).hexdigest()

def hash_file(file_object):
	"""Returns a SHA224 hash of a file, in a hex-dump string format."""
	file_data = file_object.read()
	file_object.seek(0,0)
	return hashlib.sha224(file_data).hexdigest()

def sanitize(string):
	"""
	Sanitizes a string from HTML "dangerous" stuff.
	For now, it is mapped to bleach.clean()
	"""
	return bleach.clean(string)
