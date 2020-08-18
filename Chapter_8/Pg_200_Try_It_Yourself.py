#8-3

def make_shirt(size, message):
	#Display t-shirt information
	print(f"\nT-shirt size: {size}.")
	print(f"Message: {message}.")

make_shirt('Medium', 'Hello!')

#----------------------------------------------------------------------------------
#8-4

def make_shirt( message, sizes = 'Large'):
	#Display t-shirt information
	print(f"\nT-shirt size: {sizes}")
	print(f"Message: {message}")

make_shirt('I love Python.')

make_shirt('I love python', 'Medium')

make_shirt('We all love python', 'Any Size')	

#----------------------------------------------------------------------------------
#8-5

def describe_city( city_name, country = 'Reykjavik'):
	#Display city information 
	print(f"\n{country.title()} is in {city_name.title()}.")

describe_city('iceland')

describe_city('south africa', 'pretoria')

describe_city('india','dehli')

describe_city('russia','bulgaria')

describe_city('australia','melbourne')

#----------------------------------------------------------------------------------