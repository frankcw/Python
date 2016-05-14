#While loop pizza

prompt = 'Please enter the desired toppings:'
prompt += '\n(Enter "quit" when you are done)'



while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else:
		print('You have added ' + toppings + ' to your pizza!')