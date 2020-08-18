#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

food = 'pizza'
print("\nIs food == 'pizza'? I predict True.")
print( food == 'pizza')
print("\nIs food == 'pasta'? I predict False.")
print(food == 'pasta')

place = 'Woodmead'
print("\nIs place = 'Woodmead'? I predict True.")
print(place == 'Woodmead')
print("\nIs place = 'Rivonia'? I predict False.")
print(place == 'Rivonia')

job = 'student'
print("\nIs job == 'student'? I predict True.")
print(job == 'student')
print("\nIs job == 'teacher'? I predict False.")
print(job == 'teacher')

laptop = 'acer'
print("\nIs laptop == 'acer'? I predict True.")
print(laptop == 'acer')
print("\nIs laptop == 'dell'? I predict False.")
print(laptop == 'dell')

#5-2
laptop = 'acer'
print("\nIs laptop == 'acer'? I predict True.")
print(laptop == 'acer')
print("\nIs laptop == 'dell'? I predict False.")
print(laptop == 'dell')

print("")

car = 'Audi'
print(car.lower() == 'audi')
car = 'Audi'
print(car.lower() == 'audi')


age = 18
print(age == 18)

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)


age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
