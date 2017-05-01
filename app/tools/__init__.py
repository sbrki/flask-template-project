import hashlib
import bleach

def hash(string):
	"""Returns a SHA224 hash of a string, in a hex-dump string format."""
	return hashlib.sha224(string.encode()).hexdigest()

def sanitize(string):
	"""
	Sanitizes a string from HTML "dangerous" stuff.
	For now, it is mapped to bleach.clean()
	"""
	return bleach.clean(string)