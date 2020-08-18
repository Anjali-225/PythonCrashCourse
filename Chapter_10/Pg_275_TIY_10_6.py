#10-6 = Addition
print("Give me two numbers, and I'll add them.")

try:
	first_number = input("\nEnter the first number: ")
	second_number = input("Enter the second number: ")
	
except ValueError:
	print("Please type a number!")
	
else:
	answer = int(first_number) + int(second_number)
	print(f"The answer is {answer}")
#-------------------------------------------------------------------------------