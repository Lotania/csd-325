#The purpose of this program is to demonstrate the basics of unit testing
#by acting as the test program

#call function to accept two mandatory arguments and two optional arguments
def city_country(city, country, population=0, language=""):
	print(f"{city}, {country} -- population {population}, {language}")
	
	#for unit tests, a return is required
	#return f"{city}, {country} -- population {population}, {language}"

#the following variables are to make sure the overall function works
ci1 = "Same"
co1 = "Diff"

ci2 = "Antwerp"
co2 = "Belgium"
po2 = 536079

co3 = "France"
ci3 = "Paris"
po3 = 2103000
la3 = "French"
	
city_country(ci1, co1)
city_country(ci2, co2, po2)
city_country(ci3, co3, po3, la3)