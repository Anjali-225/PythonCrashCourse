#8-14 
#8-17 This code adheres to the styling functions mentioned in this chapter
def make_car(make, model, **car_info):
	"""Build a dictionary containing everything we know about a user."""
	car_info['make'] = make
	car_info['car model'] = model
	return car_info
car = make_car('subaru', 'outback', color='blue', tow_packages=True)
print(car)
#-----------------------------------------------------------------------------------------------s