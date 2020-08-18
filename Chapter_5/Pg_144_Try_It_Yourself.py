#5-8
user_name = ['admin', 'jaden', 'courtney','anjali', 'ruben']

for name in user_name:
	if name == 'admin':
		print(f"Hello {name.title()} would you like to see a status report?")
	else:
		print(f"Hello {name.title()}, thank you for logging in again.")
print("")

#5-9
user_names = []
if len(user_names)==0:
	print("We need to find some users")
elif name == 'admin':
	print("Hello admin, would you like to see a status report?")
else:
	print(f"Hello {name}, thank you for logging in again.")
print("")

#5-10
current_users = ['Admin', 'Jaden', 'Courtney','Anjali', 'Ruben']
new_users = ['Courtney','Tash', 'Vusi','Josh', 'jaden']

for new in new_users:
	if new in current_users:
		print("You will need to enter a new username")
	else:
		print("Username is available")
print("")

#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
	if num == 1:
		print("1st")
	elif num == 2:
		print("2nd")
	elif num == 3:
		print("3rd")
	else:
		print(f"{num}th")