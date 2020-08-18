#10-3#

filename = 'guest.txt'

name = input("What is your name? ")

with open(filename, 'w') as file_object:
	file_object.write(f"{name.title()}")

#--------------------------------------------------------------------------
#10-4#
file_name = 'guest_book.txt'
new = True


while new:
	guest_name = input("\nWhat is your name? ")
	print(f"Hello {guest_name.title()}")
	repeat =  input("Add name? (yes/no) ")
	

	if repeat == 'no':
		new = False

	with open(file_name, 'a') as fileobject:
		fileobject.write(f"{guest_name.title()}\n")

#---------------------------------------------------------------------
#10-5#
file_names = 'Programming_Poll.txt'
answer = True


while answer:
	response = input("\nWhy do you like programming? ")

	repeat =  input("Add another reason? (yes/no) ")
	
	if repeat == 'no':
		answer = False

	with open(file_names, 'a') as fileobject:
		fileobject.write(f"{response}\n")
#--------------------------------------------------------------------------
'''