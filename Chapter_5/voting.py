age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

ages = 15
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")


age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")