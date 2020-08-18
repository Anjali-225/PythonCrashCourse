#4-11
MyPizzas = ['Margherita', 'Chicken Tikka', 'Vegetarian']
print(f"My pizzas: {MyPizzas}")
friend_Pizzas = MyPizzas[:]
print(f"Friends pizzas: {friend_Pizzas}\n")

MyPizzas.append("BBQ")

friend_Pizzas.append("Cheese")


print(f"\nMy favourite pizzas are:")
print(MyPizzas)

print("My friend's favorite pizzas are:")
print(friend_Pizzas)	

print("")
print("#4-12")
print("")

#4-12
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