#9-4
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
restuarant_1 = Restuarant('Salsa', 'Mexican')
restuarant_1.describe_restuarant()

print("\nNumber served: " + str(restuarant_1.number_served))
restuarant_1.number_served = 70
#restuarant_1.open_restuarant()
restuarant_1.set_number_served(120)
print("Number served: " + str(restuarant_1.number_served))

restuarant_1.increment_number_served(239)
print("Number served: " + str(restuarant_1.number_served))
#-------------------------------------------------------------------------------
print("")
#-------------------------------------------------------------------------------
restuarant_2 = Restuarant('Banjaara', 'Indian')
restuarant_2.describe_restuarant()

print("\nNumber served: " + str(restuarant_2.number_served))
restuarant_2.number_served = 50
#restuarant_1.open_restuarant()
restuarant_2.set_number_served(56)
print("Number served: " + str(restuarant_2.number_served))

restuarant_2.increment_number_served(84)
print("Number served: " + str(restuarant_2.number_served))
#-------------------------------------------------------------------------------