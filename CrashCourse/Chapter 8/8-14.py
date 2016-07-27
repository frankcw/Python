#function that stores dictionary information

def make_car(make,model,**options):
	"""function to create the car package and options with a dictionary"""
	car_descriptions = {}
	car_descriptions['car_make'] = make
	car_descriptions['car_model'] = model
	for key, value in options.items():
		car_descriptions[key] = value
	return car_descriptions

car = make_car('subaru','outback', color='blue', tow_package=True)

print(car)