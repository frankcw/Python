#if statements and lists

users=['admin','fracor','juaher','matcor']

for user in users:
	if user=='admin':
		print('Hello admin, would you like to see the status report?')
	else:
		print ("Hello user, thank you for logging in again.")
