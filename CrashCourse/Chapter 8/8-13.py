#functions with dictionaries and aribitrary keyword arguaments



def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('frank', 'cordova',
	location='south bound brook',
	field='IT')

print(user_profile)