#10-12 = Favorite Number Remembered 
import json

try:
	with open('number_10_12.json') as f:
		number = json.load(f)

except FileNotFoundError:
	number = input("What is your favourite number? ")
	with open('number_10_12.json', 'w') as f:
		json.dump(number, f)
	print(f"\nYour favorite number is {number}.")
	print('We will remember that!')

else:
	print(f"I know your favourite number. It's {number}.")

#-------------------------------------------------------------------------------