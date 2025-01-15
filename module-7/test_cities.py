#The purpose of the program is to demonstrate the basics of unit testing
#by acting as the program that will test a function of city_functions

#import required library
import unittest

#import function from target program
from city_functions import city_country

#declare method to test
class test_city_country(unittest.TestCase):
	#two tests, using the imported city-country function
	def test_first(self):
		self.assertEqual((city_country("Same","Same", 987655678)), "Same, Same -- population 987655678, ")
		
	def test_actual(self):
		self.assertEqual((city_country("Seoul","South Korea", 51700000, "Korean")), "Seoul, South Korea -- population 51700000, Korean")

#boilerplate code to protect from unintended code execution
if __name__ == '__main__':
	unittest.main()