#9-10 = Class
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