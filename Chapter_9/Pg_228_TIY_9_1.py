#9-1
class Restuarant:

	def __init__(self, restuarant_name, cuisine_type):
		"""Initialize restuarant_name and cuisine_type attributes."""
		self.restuarant_name = restuarant_name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restuarant(self):
		print(f"{self.restuarant_name} serves {self.cuisine_type}.")

	def open_restuarant(self):
		print(f"{self.restuarant_name} is open!")

restuarant = Restuarant('perfect pizza', 'italian')

print(f"My restuarant's name is {restuarant.restuarant_name}.")
print(f"The restuarant serves {restuarant.cuisine_type} cuisine.\n")

restuarant.describe_restuarant()
restuarant.open_restuarant()

#-------------------------------------------------------------------------------