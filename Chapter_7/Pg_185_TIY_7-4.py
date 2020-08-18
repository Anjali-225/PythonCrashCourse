#7-4
#---------------------------------------------------------------------

prompt = "\nPlease enter a topping you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"Adding {topping.title()} as your topping")	
#---------------------------------------------------------------------