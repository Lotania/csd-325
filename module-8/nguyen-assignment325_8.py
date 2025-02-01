#Anthony Nguyen, assignment 8
#The purpose of this program is to demonstrate the basics of
#JSON file handling via Python.

#import library containing load, dump, etc
import json

#create json constructor class for data from file
class file_class:
	def __init__(self, f_name, l_name, student_ID, email):
		self.f_name = f_name;
		self.l_name = l_name;
		self.student_ID = student_ID;
		self.email = email;

#assign file name to variable to make it easier to call
file_path = 'student.json'

#load file data to data variable
with open(file_path) as f:
	data = json.load(f)

#this list will store data from the file
objects = []

#function that appends data variable to list
def objects_data(data):
	for item in data:
		obj = file_class(item['F_Name'], item['L_Name'], item['Student_ID'], item['Email'])
		objects.append(obj)
		

#print function
def print_data(objects):
	for obj in objects:
		print(obj.f_name + " " + obj.l_name + ", ID: " + str(obj.student_ID) + ", email: " + obj.email)


#load and display contents of variable
print("This is the original Student list.")
objects_data(data)
print_data(objects)
print()

#add the following dictionary to the data variable
objects.append(file_class("Anthony", "Nguyen", 29827, "annthoygunyen@gmail.com"))

#load and display new contents of variable
print("This is the updated Student list.")
print_data(objects)
print()

#attempt to write updated data to file
try:
	with open(file_path, "w") as f:
		json.dump(data, f, indent=4)
	
	print("The .json file has been updated.")

except Exception:
	print("OPERATION FAILED")