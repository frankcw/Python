#create more instances from the 9-1 class

class Restaurant():
	def __init__(self,restaurant_name,restaurant_cuisine):
		'''Initialize the name and the cuisine'''
		self.name = restaurant_name
		self.cuisine = restaurant_cuisine

	def describe_restaurant(self):
		print(self.name.title() + ' is the name of the restaurant, ' + 
			'and we serve ' + self.cuisine + ' food.')
	def open_restaurant(self):
		print('The restaurant is open!')

restaurant1 = Restaurant('burger king','exquicit delicacy')
restaurant2 = Restaurant('applebees','frozen food')
restaurant3 = Restaurant('McDonalds','more burgers')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

