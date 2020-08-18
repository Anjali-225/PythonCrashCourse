#4-14 Read through it all 
################################
#4-15
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(f"The first three items in the list are: {players[0:3]}")

print("")

print(f"Three items from the middle of the list are: {players[1:4]}")

print("")

print(f"The last three items in the list are: {players[-3:]}") 

################################
simple_foods = ('potatoes', 'rice', 'soup', 'sandwiches', 'sauce')

for food in simple_foods:
	print(food)

#simple_foods[0] = 'mash'

print("")

simple_foods = ('mash','rice','soup','pizza','sandwiches')

for food in simple_foods:
	print(food)

###############################

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
for food in my_foods:
	print(f"{food}")

print("")

print("My friends favorite foods are: ")
for foods in friend_foods:
	print(f"{foods}")