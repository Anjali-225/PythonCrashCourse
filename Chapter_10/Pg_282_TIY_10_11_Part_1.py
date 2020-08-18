#10-11 = Favorite Number = Part 1
import json

#ASKED THE USER FOR THEIR FAVOURITE NUMBER
favorite_number = int(input("What is your favorite number? "))

#CREATED A FILE CALLED THIS:
filename = 'number_10_11.json'

#OPENING FILE AND "DUMPING" THE INFO WE JUST RECEIVED
with open(filename, 'w') as f:
	json.dump(favorite_number, f)
	print(f"\nYour favorite number is {favorite_number}.")
	print('We will remember that!')
#-------------------------------------------------------------------------------