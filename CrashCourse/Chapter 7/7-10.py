#inputing with a while loop and a dictionary

#state the dictionary
polling = {}
#set the boolean for the while loop so you can later break it
polling_active = True


while polling_active:
	name = input('\nWhat is your name? ')
	response = input("\nWhat is the only one place you would like to visit? ")

	#build the dictionary
	polling[name] = response

	#break the loop
	more_polling = input('\nIs there someone else that wants to participate on the poll?' + 
		' (yes/no) ')
	if more_polling == 'no':
		polling_active = False 

print('\n----Polling Results----')

#print the statements of the dictionary
for name, place in polling.items():
	print(name.title() + ' would like to visit ' + place.title() + "!")	