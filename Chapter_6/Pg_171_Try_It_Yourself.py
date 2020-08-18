#6-7
person1 = {'first_name' : 'Anjali', 'age' : 18, 'city' : 'Rivonia'}
person2 = {'first_name' : 'Roshni', 'age' : 30, 'city' : 'Delhi'}
person3 = {'first_name' : 'Aman', 'age' : 24, 'city' : 'Mumbai'}

people =[person1, person2, person3]

for person in people:
	print(person)
#----------------------------------------------------------------------------------
#6-8
print("")

pet1 ={'pet' : 'dog', 'owner' : 'Anjali'}
pet2 ={'pet' : 'cat', 'owner' : 'Roshni'}
pet3 ={'pet' : 'fish', 'owner' : 'Aman'}

pets = [pet1,pet2,pet3]

for pet in pets:
	print(pet)
	for  pett, Oname in pets:
		print(f"{Oname.title()} owns a {pett.title()}.")
#----------------------------------------------------------------------------------
#6-9
print("")

favorite_places = {'Anjali' : 'Spain', 'Payal' : 'Greece','Malay': 'India'}

for name, place in favorite_places.items():
	print(f"{name.title()}'s favorite place is {place.title()}.")

#----------------------------------------------------------------------------------
#6-10
print("")

favorite_number = {'jen': [13, 45] , 'sarah' : [5, 67], 'edward' : [16, 22] ,'phil' : [21,87] }

for name, numbers in favorite_number.items():
	print(f"\n{name.title()}'s favorite n numbers are:")
	for num in numbers:
		print(f"\t{num}")

#----------------------------------------------------------------------------------
#6-11
print("")
cities ={
	'america' :{
		'country' : 'texas'            ,
		'population' : 20_000            ,
		'fact' : 'It\'s in North America',
			},
	'russia' :{ 
		'country' : 'poland',
		'population' : 10_500,
		'fact' : 'It\'s in Asia' ,
			},
	'south africa' :{
		'country' : 'pretoria',
		'population' : 70_000     ,
		'fact' : "It\'s in Africa",
			},
		}

for city, city_info in cities.items():
	print(f"\nName of city: {city.title()}")
	country = f"{city_info['country']}"
	population = city_info['population']
	fact = f"{city_info['fact']}"
	print(f"\tCountry: {country.title()}")
	print(f"\tPopulation: {population}")
	print(f"\tFact: {fact}")

#----------------------------------------------------------------------------------
#6-12
print("")
number ={
	'jen' :{
		'lucky_number' : 13  ,
		'unlucky_number' : 45 ,
		'favorite_number' : 5 ,
			},
	'sarah' :{ 
		'lucky_number' : 67  ,
		'unlucky_number' : 16 ,
		'favorite_number' : 22 ,
			},
	'edward' :{
		'lucky_number' : 21 ,
		'unlucky_number' : 87 ,
		'favorite_number' : 50 ,
			},
	'phil' :{
		'lucky_number' : 12  ,
		'unlucky_number' : 4 ,
		'favorite_number' : 56 ,
			},
		}

for name, num_info in number.items():
	print(f"\nName: {name.title()}")
	luckyNum = f"{num_info['lucky_number']}"
	unluckyNum = f"{num_info['unlucky_number']}"
	favNum = f"{num_info['favorite_number']}"
	print(f"\tLucky Number: {luckyNum}")
	print(f"\tUnlucky Number: {unluckyNum}")
	print(f"\tFavorite Number: {favNum}")

#----------------------------------------------------------------------------------