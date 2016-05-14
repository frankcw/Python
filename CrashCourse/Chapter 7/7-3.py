#Multiple of Ten using modulus

number = input('Please enter a number:')
number = int(number)

result = number % 10

if result == 0:
	print('This number is multiple of 10')
else:
	print('This number is not a multiple of 10')