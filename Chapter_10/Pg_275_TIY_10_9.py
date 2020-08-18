#10-9 = Silent Cats and Dogs:
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

	try :
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
			

	except FileNotFoundError:
		#TO FAIL SILENTLY
		pass
		#print(f"Sorry, the file {filename} does not exist.")
		
	else:
		print(f"\nReading File: {filename}")
		print(f"------------------------")
		print(contents)
#-------------------------------------------------------------------------------