#If..Then..Else (conditionals)
#espressions: is any legal combination of symbols that represents a value
#statements: can run

name = input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age > 20:
	print(name, 'you are older than 20 years old!')
	print('What would you like to drink?')
elif age >= 18:
	print('You are allowed in,')
	print('But you are not allowed to drink, please feel free to dance')
else:
	print('Unfortunately',name,'you are younger than 20.')
	

