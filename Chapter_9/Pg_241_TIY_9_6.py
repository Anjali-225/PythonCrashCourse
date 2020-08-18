#9-6
class Restuarant:

	def __init__(self, restuarant_name, cuisine_type):
		"""Initialize restuarant_name and cuisine_type attributes."""
		self.restuarant_name = restuarant_name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 0

	def describe_restuarant(self):
		print(f"{self.restuarant_name} serves {self.cuisine_type}")
	
	def open_restuarant(self):
		print(f"{self.restuarant_name} is open!\n")

	def set_number_served(self, number_served):
		#Allow user to set number of customers that have been served
		self.number_served = number_served

	def increment_number_served(self, add_served):
		"""Add the given amount to the odometer reading."""
		self.number_served += add_served

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

class IceCreamStand(Restuarant):
	'''Represents the ice cream stand'''
	def __init__(self, restuarant_name, cuisine_type='Ice_Cream'):
		"""Initialize attributes of the parent class."""
		super().__init__(restuarant_name, cuisine_type)
		self.flavours = []

	def show_flavours(self):
		#Display the flavours that are available
		print("\nWe have the following ice cream flavours available: ")
		for flavour in self.flavours:
			print(f"- {flavour.title()}")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

ice_cream_1 = IceCreamStand('Polar Bear')
ice_cream_1.flavours =['vanilla', 'chocolate', 'bubblegum']

ice_cream_1.describe_restuarant()
ice_cream_1.show_flavours()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------