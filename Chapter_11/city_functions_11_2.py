#11-2 = Function
#FAILED Function
'''
def city_country_pop(city_name, country_name, population):
	"""Generate a neatly formatted city, country and population."""
	country_city_pop = f"{city_name}, {country_name} = {population}."
	return city_country_pop.title()
'''
#-------------------------------------------------------------------------------
def city_country_pop(city_name, country_name, population=''):
	"""Generate a neatly formatted city, country and populations."""
	if population:
		country_city_pop = f"{city_name}, {country_name} - "f"Population = {population}"
	else:
		country_city_pop = f"{city_name}, {country_name}"
	return country_city_pop.title()
#-------------------------------------------------------------------------------