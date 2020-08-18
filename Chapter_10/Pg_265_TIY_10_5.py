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