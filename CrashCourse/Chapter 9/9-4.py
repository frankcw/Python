#classes with default argument

class Restaurant():
	def __init__(self,restaurant_name,restaurant_cuisine, number_served = 0):
		'''Initialize the name and the cuisine'''
		self.name = restaurant_name
		self.cuisine = restaurant_cuisine

	def describe_restaurant(self):
		print(self.name.title() + ' is the name of the restaurant, ' + 
			'and we serve ' + self.cuisine + ' food.')
	def open_restaurant(self):
		print('The restaurant is open!')

	def restaurant

restaurant = Restaurant('burger king','exquicit delicacy')
restaurant.describe_restaurant()
restaurant.open_restaurant()
		