#9-13 
from random import randint
#-------------------------------------------------------------------------------
class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_dice(self):
		number = randint(1, self.sides)
		return (number)
#-------------------------------------------------------------------------------
dice6 = Die()
#-------------------------------------------------------------------------------
results = []
#-------------------------------------------------------------------------------
for roll in range(10):
	result = dice6.roll_dice()
	results.append(result)

print("10 rolls of a 6-sided dice:")
print(results)
#-------------------------------------------------------------------------------

dice10 = Die(sides= 10)
#-------------------------------------------------------------------------------
results = []
#-------------------------------------------------------------------------------
for roll in range(10):
	result = dice10.roll_dice()
	results.append(result)

print("\n10 rolls of a 10-sided dice:")
print(results)
#-------------------------------------------------------------------------------

dice20 = Die(sides = 20)
#-------------------------------------------------------------------------------
results = []
#-------------------------------------------------------------------------------
for roll in range(10):
	result = dice20.roll_dice()
	results.append(result)

print("\n10 rolls of a 20-sided dice:")
print(results)
#-------------------------------------------------------------------------------