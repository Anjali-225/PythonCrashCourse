#10-11 = Favorite Number = Part 2
import json

#USING THIS FILE
filename = 'number_10_11.json'

#GETTING THE INFO FORM FILE AND USING IT
with open(filename) as f:
	number = json.load(f)
	print(f"I know your favorite number! It's {number}.")
#-------------------------------------------------------------------------------