#deleting using a while loop

#creating two lists, one that has the items and an empty one
various_sandwiches = ['pastrami','chicken parm','grilled cheese',
	'ham','pastrami','tuna','pbj','pastrami']

print('We recently ran out of pastrami')

while 'pastrami' in various_sandwiches:
	various_sandwiches.remove('pastrami')

print('\nThese are the only types available:')
for sandwich in various_sandwiches:
	print(sandwich)

