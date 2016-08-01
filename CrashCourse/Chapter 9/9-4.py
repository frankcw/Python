#classes with default argument

class Restaurant():
	def __init__(self,restaurant_name,restaurant_cuisine):
		'''Initialize the name and the cuisine'''
		self.name = restaurant_name
		self.cuisine = restaurant_cuisine
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name.title() + ' is the name of the restaurant, ' + 
			'and we serve ' + self.cuisine + ' food.')
	def open_restaurant(self):
		print('The restaurant is open!')

	def restaurant(self):
		'''Print statement showing how many customers have been served'''
		print('The restaurant has served ' + str(self.number_served) + ' customers')


	def set_number_served(self,served):
		'''setting the number of served customers'''
		self.number_served = served

	def increment_number_served(self, served):
		'''incrementing the original instance, which is already modified in the before method'''
		self.number_served += served



food_restaurant = Restaurant('burger king','exquicit delicacy')
food_restaurant.describe_restaurant()
food_restaurant.open_restaurant()

#Changing the value of a variable by calling the Class
#THIS IS AN OPTIONAL CALL = food_restaurant.number_served = 2
#Calling the new method with the changed value
food_restaurant.set_number_served(3)
food_restaurant.restaurant()

food_restaurant.increment_number_served(5)
food_restaurant.restaurant()
		