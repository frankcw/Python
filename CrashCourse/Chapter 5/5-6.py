#if statements with variables that are numbers

#change variable for different results
age=65

if age < 2:
	print('Person is a baby.')
elif age >4 and age <13:
	print('Person is todler.')
elif age >= 13 and age <20:
	print('Person is a teenager')
elif age >= 20 and age < 65:
	print('Person is an adult')
else:
	print('Person is an elder')