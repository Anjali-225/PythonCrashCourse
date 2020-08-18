import json
#USING THIS FILE
filename = 'username.json'
#GETTING THE INFO FORM FILE AND USING IT
with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}!")