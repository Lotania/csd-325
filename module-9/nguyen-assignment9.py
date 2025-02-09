#Anthony Nguyen, assignment 9, 02/07/2025
#The purpose of the program is to demonstrate the basics of API requests

#import required libraries for using json files and APIs
import requests
import json

#function to format output from json file
def format_print(jason):
	text = json.dumps(jason, sort_keys=True, indent=4)
	print(text)
	
#make a request to access an API, and print the status of the request
response = requests.get('https://swapi.dev/api/')
print(response.status_code)

#print as is
print(response.json())
#print formatted output
format_print(response.json())