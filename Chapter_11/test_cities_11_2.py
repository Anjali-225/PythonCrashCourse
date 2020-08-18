#11-2 = Test
#FAILED TEST
'''
import unittest
from city_functions_11_2 import city_country_pop

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_function_11_2.py'."""

	def test_city_country(self):
		"""Do city, country names like 'Santiago, Chile' work?"""
		formatted_city_country = city_country_pop('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()
'''
#-------------------------------------------------------------------------------

import unittest
from city_functions_11_2 import city_country_pop

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_functions_11_2.py'."""

	def test_city_country(self):
		"""Do city, country names like 'Santiago, Chile' work?"""
		formatted_city_country = city_country_pop('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do city, country names ans population like 'Santiago, Chile - Population = 500000' work?"""
		formatted_city_country_pop = city_country_pop('santiago', 'chile', 500000)
		self.assertEqual(formatted_city_country_pop, 'Santiago, Chile - Population = 500000')

if __name__ == '__main__':
	unittest.main()
#-------------------------------------------------------------------------------