#function calling a city and a country

def city_country(city,country):
	print(city.title() + ', ' + country.title())

while True:
	print('\nHit "q" to exit')
	city = input('Please enter a city:')
	if city == 'q':
		break
	country = input('Please enter the country the city belongs to:')
	if country == 'q':
		break
	describe_city(city,country)