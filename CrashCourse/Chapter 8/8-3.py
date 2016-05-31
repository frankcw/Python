#function that acepts lists and dictionaries

def make_shirt(shirt_size,shirt_message):
	"""shirt with message function"""
	print('\nYour shirt size is ' + shirt_size + '.')
	print('\nThe message printed on the shirt will be "' + shirt_message + '".')

make_shirt(str(8),"Frank's Shirt")
make_shirt(shirt_size="10",shirt_message="I like my shirt!")