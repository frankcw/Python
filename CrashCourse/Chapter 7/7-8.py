#while loops with lists 

#creating two lists, one that has the items and an empty one
various_sandwiches = ['chicken parm','grilled cheese','ham','tuna','pbj']
sandwich_made = []

#moving the items from one list to another one
while various_sandwiches:
	sandwich = various_sandwiches.pop()
	print('I made your ' + sandwich + ' sandwich.')
	sandwich_made.append(sandwich)

#statement showing the new list items
for final_sandwich in sandwich_made:
	print (final_sandwich.title() + ' sanwich was made.')




