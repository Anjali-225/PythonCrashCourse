#6-4
programming_languages ={'list' : 'group of variables',
						 'dictionary' : 'like an objects',
						  'loops':'runs through a list',
						  'prints':'document_write',
						  'tuple':'unchangeble list'}

for k, v in programming_languages.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")

#----------------------------------------------------------------------------------
#6-5
print("")

rivers = {'nile' : 'egypt','orange river' : 'south africa', 'amazon river': 'south america'}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

for riv in rivers.keys():
	print(f"{riv.title()}")

for countries in rivers.values():
	print(f"{countries.title()}")
#----------------------------------------------------------------------------------
#6-6
print("")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'anjali':'sql'
}

favorite_language_poll = ['jen', 'jess', 'edward', 'sam']

for poll in favorite_language_poll:
	if poll in favorite_languages.keys():
		print(f"Thank you {poll.title()} for responding") 
	else:
		print(f"{poll.title()}, you are invited to take the poll")

print("")
#----------------------------------------------------------------------------------