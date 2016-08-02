from name_function import get_formatted_name

print('Enter "q" at any time to quit.')
while True:
	first = input("\nPlease provide a first name: ")
	if first == 'q':
		break
	last = input('Please provide your last name: ')
	if last == 'q':
		break

	formatted_name = get_formatted_name(first,last)
	print('\nNeatly formatted name: ' + formatted_name + '.')