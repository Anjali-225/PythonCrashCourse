#10-8 = Cats and Dogs
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	print(f"\nReading File: {filename}")
	print(f"------------------------")

	try :
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
			print(contents)

	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
		
#-------------------------------------------------------------------------------
files = ['cats.txt', 'dog.txt']

for file in files:
	print(f"\nReading File: {file}")
	print(f"------------------------")

	try :
		with open(file, encoding='utf-8') as f:
			content = f.read()
			print(content)

	except FileNotFoundError:
		print(f"Sorry, the file {file} does not exist.")
#-------------------------------------------------------------------------------