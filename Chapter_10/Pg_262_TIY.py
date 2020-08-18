#10-1#
#With Block- reading entire files content#
print("Reading in the entire file's content:")

with open('learning_python.txt') as file_object:
	contents = file_object.read()

print(f"{contents}")
#--------------------------------------------------------------------------
#By Looping over the file#
print("\nLooping over the file object:")

filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
#--------------------------------------------------------------------------
#Storing lines in a list
filename = 'learning_python.txt'

print("\nStoring lines in a list:")

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(f"{line.rstrip()}")
#--------------------------------------------------------------------------
print("")
#--------------------------------------------------------------------------
#10-2#
filename = 'learning_python.txt'

with open (filename) as file_objects:
	for line in file_objects:
		lin = line.replace('Python', 'C')
		print(lin.rstrip())
#--------------------------------------------------------------------------
