#function with many arguments

def make_sandwich(size,*ingredients):
	"""Summary of the sandwich to be created"""
	print('Making a ' + str(size) + 
		'inch sandwich with the following ingredients')
	for ingredient in ingredients:
		print('-' + ingredient.title())

make_sandwich(6,'tomato','lettuce','bacon')
make_sandwich(12,'roast beef','chicken')