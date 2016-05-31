#function that acepts lists and dictionaries

def make_shirt(shirt_size='large',shirt_message='I love Python!'):
	"""shirt with message function"""
	print('\nYour shirt size is ' + shirt_size.title() + '.')
	print('\nThe message printed on the shirt will be "' + shirt_message + '".')

make_shirt()
make_shirt(shirt_size="medium",shirt_message="I like my shirt!")
make_shirt('small','This message is a test!')