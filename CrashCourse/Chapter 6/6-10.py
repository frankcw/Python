#loops with numbers

favorite_numbers={
	'frank':8,
	'claudia':3,
	'matteo':4,
	'isabel':5,
	'carlos':3}

for name, number in favorite_numbers.items():
	print(name.title() + "'s favorite number is " +
	str(number) + ".")