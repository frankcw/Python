#Functions with default values

def describe_city(city,country='Iceland'):
	print(city.title() + ' is in ' + country.title() + '.')

describe_city('guayaquil','ecuador')
describe_city('Reykjavik')
describe_city('new york','USA')