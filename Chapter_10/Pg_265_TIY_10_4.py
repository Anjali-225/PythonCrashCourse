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
