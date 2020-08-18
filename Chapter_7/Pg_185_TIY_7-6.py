'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each
of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit'
value.
'''

#WHILE#---------------------------------------------------------------------

prompt = "\nEnter your age: "
prompt += "\nEnter '0' to end the program."

while input !=0: #this conndition is used to stop the loop 
	age = int(input(prompt))
	if age > 0 and age < 3:
		print("The ticket is free")
	elif age >= 3 and age <= 12:
		print("The ticket costs $10")
	elif age > 12:
		print("The ticket costs $15")

	if age == 0:
		break
#---------------------------------------------------------------------

#ACTIVE#-------------------------------------------------------------------

prompt = "\nPlease enter a topping you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "
active = True
while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print(f"Adding {topping.title()} as your topping")

#-------------------------------------------------------------------

#BREAK#-------------------------------------------------------------

prompt = "\nPlease enter a topping you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"Adding {topping.title()} as your topping")	

#-------------------------------------------------------------------