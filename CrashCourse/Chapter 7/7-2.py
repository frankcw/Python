#restaurant seating input with if

people_count = input('How many people are you having dinned with?')
people_count = int(people_count)

if people_count >= 8:
	print('You will have to wait for a table.')
else:
	print('Go right ahead. You will be seated.')
