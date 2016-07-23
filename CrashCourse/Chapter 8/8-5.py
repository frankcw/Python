#Functions with default values

def describe_city(city,country='Iceland'):
	print(city.title() + ' is in ' + country.title() + '.')

while True:
	print('\nHit "q" to exit')
	city = input('Please enter a city:')
	if city == 'q':
		break
	country = input('Please enter the country the city belongs to:')
	if country == 'q':
		break
	describe_city(city,country)


#describe_city('guayaquil','ecuador')
#describe_city('Reykjavik')
#describe_city('new york','USA')