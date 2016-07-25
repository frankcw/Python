#while loops with Movie Tickets

prompt = input('what is your age?')

age = int(prompt)

while True:
	age = int(prompt)
	if age < 3:
		print('Your ticket is free.')
	elif age <= 12:
		print("Your ticket is $10.")
	else:
		print("Your ticket will be $15")
	break

