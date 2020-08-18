#9-2
class Restuarant:

	def __init__(self, restuarant_name, cuisine_type):
		self.restuarant_name = restuarant_name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restuarant(self):
		print(f"\n{self.restuarant_name} serves execellent {self.cuisine_type}.")

	def open_restuarant(self):
		print(f"{self.restuarant_name} is open!")
#-------------------------------------------------------------------------------
restuarant_1 = Restuarant('perfect pizza', 'italian')
#restuarant_1.open_restuarant()
restuarant_1.describe_restuarant()
#-------------------------------------------------------------------------------
restuarant_2 = Restuarant('classic', 'indian')
#restuarant_2.open_restuarant()
restuarant_2.describe_restuarant()
#-------------------------------------------------------------------------------
restuarant_3 = Restuarant('salsa', 'mexican')
#restuarant_3.open_restuarant()
restuarant_3.describe_restuarant()
#-------------------------------------------------------------------------------