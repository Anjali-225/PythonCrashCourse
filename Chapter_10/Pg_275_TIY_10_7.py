#10-7 = Addition Calculator
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nEnter the first number: ")

	if first_number == 'q':
		break

	second_number = input("Enter the second number: ")

	if second_number == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Please type a number!")
	else:
		print(f"The answer is {answer}")
#-------------------------------------------------------------------------------