#list with loops and a slice 

pizzas=['cheese','sausage','beef','chicken']
friend_pizzas=pizzas[:]

pizzas.append('ham')
friend_pizzas.append('buffalo')

for pizza in pizzas:
	print('My favorite pizzas are '+pizza)
print("\n")
for fpizza in friend_pizzas:
	print('My friends pizzas are '+fpizza)