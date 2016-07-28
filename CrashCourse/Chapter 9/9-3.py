#classes for users

class User():
	def __init__(self, first_name, last_name, city_from, country_born):
		"""user class initializing"""
		self.first = first_name
		self.last = last_name
		self.city = city_from
		self.country = country_born

	def describe_user(self):
		print('\n' + self.first.title() + ' ' + self.last.title() + 
			" is from " + self.city.title() + ', ' + 
			self.country.title() + '.')

	def greet_user(self):
		print('Hello ' + self.first.title() + 
			', thanks for using this script.')


frank = User('frank','cordova','guayaquil','ecuador')
frank.describe_user()
frank.greet_user()

claudia = User('claudia','rivadeneira','riobamba','ecuador')
claudia.describe_user()
claudia.greet_user()