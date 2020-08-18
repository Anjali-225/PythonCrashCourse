'''
import json

#ASKED THE USER FOR THEIR NAME
username = input("What is your name? ")

#CREATED A FILE CALLED THIS:
filename = 'username.json'

#OPENING FILE AND "DUMPING" THE INFO WE JUST RECEIVED
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We'll remember you when you come back, {username}!")
'''
import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")                                                                                       