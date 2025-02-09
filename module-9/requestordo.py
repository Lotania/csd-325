import requests
import json

def format_print(jason):
	text = json.dumps(jason, sort_keys=True, indent=4)
	print(text)

response = requests.get('http://api.open-notify.org/astros')
print(response.status_code)
print(response.json())

format_print(response.json())