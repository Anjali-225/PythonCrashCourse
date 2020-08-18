#11-1 = Test
import unittest

from city_functions_11_1 import city_country

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_functions_11_1.py'."""

	def test_city_country(self):
		"""Do names like 'Santiago and Chile' work?"""
		formatted_city_country = city_country('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')


if __name__ == '__main__':
	unittest.main()

#-------------------------------------------------------------------------------