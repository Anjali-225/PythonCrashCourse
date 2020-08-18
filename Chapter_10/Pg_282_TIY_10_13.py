#10-13 = Verify User

import json

def get_stored_username():
	#Get username if available
	filename = 'username_10_13.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
#-------------------------------------------------------------------------------
def get_new_username():
	#Ask for new username

	filename = 'username_10_13.json'
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username
#-------------------------------------------------------------------------------
def greet_user():
	#Greet the user by their name
	username = get_stored_username()
	if username:
		verify = input(f"Are you {username.title()}? (y/n) ")
		if verify =='y':
			print(f"Welcome back, {username.title()}!")
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back, {username.title()}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username.title()}!")
#-------------------------------------------------------------------------------
greet_user()
#-------------------------------------------------------------------------------