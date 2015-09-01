#loops, good example

num = 90 #a number greater than 2 and less than 10
prime = True #aboolean to remember if this number is prime or not

for test in range(2,num):

	if num % test == 0 and num != test:
		print(num,'equals',test, '*', int(num/test))
		prime = False
		break

if prime:
	print(num,'is a prime number!')
else:
	print(num,'is not a prime number')