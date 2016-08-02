#classes for users with login nattempts

class User():
	def __init__(self, first_name, last_name, city_from, country_born):
		"""user class initializing"""
		self.first = first_name
		self.last = last_name
		self.city = city_from
		self.country = country_born
		self.login_attempts = 0

	def describe_user(self):
		print('\n' + self.first.title() + ' ' + self.last.title() + 
			" is from " + self.city.title() + ', ' + 
			self.country.title() + '.')

	def greet_user(self):
		print('Hello ' + self.first.title() + 
			', thanks for using this script.')

	def increment_login_attempts(self,attempts = 1):
		self.login_attempts += attempts
		print(self.first + ' has attempted to log in ' + str(self.login_attempts) +
		" times.")


	def reset_login_attempts(self):
		self.login_attempts = 0
		print('Login attempts have been reset to ' + str(self.login_attempts))
		

frank = User('frank','cordova','guayaquil','ecuador')
frank.describe_user()
frank.greet_user()
frank.increment_login_attempts()
frank.increment_login_attempts()
frank.increment_login_attempts()
frank.increment_login_attempts(10)
frank.reset_login_attempts()



