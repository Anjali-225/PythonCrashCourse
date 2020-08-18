#THIS IS ONLY TO READ THE CONTENTS FROM THE FILE
#-------------------------------------------------------------------------------
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)
#-------------------------------------------------------------------------------
print(contents.rstrip())
#-------------------------------------------------------------------------------
file_path = 'C:/Users/anjali/Desktop/Python/Chapter_10/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents)
#-------------------------------------------------------------------------------
filename = 'pi_digits.txt'
#-------------------------------------------------------------------------------
#TO READ IT LINE BY LINE
#-------------------------------------------------------------------------------
with open(filename) as file_object:
	for line in file_object:
		print(line)
#-------------------------------------------------------------------------------
filename = 'pi_digits.txt'
#-------------------------------------------------------------------------------
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
#-------------------------------------------------------------------------------
filename = 'pi_digits.txt'
#-------------------------------------------------------------------------------
with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.rstrip())
#-------------------------------------------------------------------------------