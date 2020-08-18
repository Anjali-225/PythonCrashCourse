#11_3 = Test
import unittest
from employee_function_11_3 import Employee

class EmployeeTestCase(unittest.TestCase):
	#Test for employee_function_11_3.py

	def setUp(self):
		#Create an employee to use in test
		self.employee_1 = Employee('Willie', 'Williams', 10000)

	def test_give_default_raise(self):
		#Test Default works correctly
		self.employee_1.give_raise()
		self.assertEqual(self.employee_1.annual_salary, 15000)

	def test_give_custom_raise(self):
		self.employee_1.give_raise(15000)
		self.assertEqual(self.employee_1.annual_salary,25000)


if __name__ == '__main__':
	unittest.main()
#-------------------------------------------------------------------------------