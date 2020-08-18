#10-10 = Common Words:

def common_count_words(filename, word):
	"""Count the approximate number repititve word in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()

	except FileNotFoundError:
		pass

	else:
		words_count = contents.lower().count(word)
		print(f"\nThe word '{word}' appears in {filename} about {words_count} times.")

#-------------------------------------------------------------------------------
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	common_count_words(filename, 'the')
	common_count_words(filename, 'then')
	common_count_words(filename, 'there')
	common_count_words(filename, 'the ')
#-------------------------------------------------------------------------------