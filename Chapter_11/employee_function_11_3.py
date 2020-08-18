#11-3 = Function
class Employee:
	'''Class to represent an employee.'''
	def __init__(self, first_name, last_name, annual_salary):
		#Initialize
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.annual_salary = annual_salary

	def give_raise(self, add_amount=5000):
		self.annual_salary += add_amount
#-------------------------------------------------------------------------------