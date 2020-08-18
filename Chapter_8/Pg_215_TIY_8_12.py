#8-12
#8-17 This code adheres to the styling functions mentioned in this chapter

def make_sandwich(*fillings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a sandwich with the following filling/s:")
	for filling in fillings:
		print(f"- {filling}")
make_sandwich('tomatoes')
make_sandwich('lettuce', 'mayonnaise', 'cheese', 'chicken')

#-------------------------------------------------------------------
