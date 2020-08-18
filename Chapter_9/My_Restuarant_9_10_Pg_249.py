#9-10 = Import
from Restuarant_9_10_Pg_249 import Restuarant
#-------------------------------------------------------------------------------
restuarant_1 = Restuarant('Salsa', 'Mexican')
restuarant_1.describe_restuarant()
restuarant_1.open_restuarant()

print("\nNumber served: " + str(restuarant_1.number_served))
restuarant_1.number_served = 70

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
