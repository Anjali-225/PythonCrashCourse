#6-1
person = {'first_name' : 'Anjali', 'age' : 18, 'city' : 'Rivonia'}
print(person)
print(person['first_name'])
print(person['age'])
print(person['city'])

for k, v in person.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")
#----------------------------------------------------------------------------------
print("")

#6-2
favorite_number = {'Courtney': 13, 'Anjali' : 5, 'Ruben' : 16, 'Vusi' : 21}
print(f"Anjali {favorite_number['Anjali']}")
print(f"Ruben {favorite_number['Ruben']}")
print(f"Courtney {favorite_number['Courtney']}")
print(f"Vusi {favorite_number['Vusi']}")

for k, v in favorite_number.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")

print("")
#----------------------------------------------------------------------------------
#6-3
programming_languages ={'list' : 'group of variables',
						 'dictionary' : 'like an objects',
						  'loops':'runs through a list',
						  'prints':'document_write',
						  'tuple':'unchangeble list'}

print(f"list: {programming_languages['list']}\n")
print(f"dictionary: {programming_languages['dictionary']}\n")
print(f"loops: {programming_languages['loops']}\n")
print(f"prints: {programming_languages['prints']}\n")
print(f"tuple: {programming_languages['tuple']}\n")

for k, v in programming_languages.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")

print("")
#----------------------------------------------------------------------------------