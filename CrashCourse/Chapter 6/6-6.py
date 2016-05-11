#

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

user_list = ['jen','frank','phil','karla']


#comparing the user_list to the key in the favorite_languages dictionary
for user in user_list:
	if user in favorite_languages:
		print(user.title() + ", thanks for taking the survey.")
	else:
		print(user.title() + ", you still need to take the survey.")