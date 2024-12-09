class Student:
	def __init__(self, f_name, l_name):
		self.f_name = f_name #first name
		self.l_name = l_name #last name
		
	def initiation(self):
		print(f"Let's get your first class's score, {self.f_name}.")
	
	def gather_score(self):
		
		all_course_hours = 0
		all_course_point = 0
		course_continue = True 
		course_limit = 0
		
		while(course_continue == True):
			cred_hr=input("How many credit hours was this class? ")

			is_valid=False 
			while(is_valid==False):
				if(cred_hr.isnumeric()): 
					if(int(cred_hr) >= 1 and int(cred_hr) <= 5):
						is_valid=True
					else:
						is_valid=False
						print("INVALID INPUT")
						cred_hr=input("How many credit hours was this class? ")
				else:
					is_valid=False
					print("INVALID INPUT")
					cred_hr=input("How many credit hours was this class? ")

			score=input("What was your score for this class? ")

			is_valid=False 
			while(is_valid==False):
				if(score.isnumeric()):
					if(int(score) >= 0 and int(score) <= 100):
						is_valid=True
					else:
						is_valid=False
						print("INVALID INPUT")
						score=input("What was your score for this class? ")
				else:
					is_valid=False
					print("INVALID INPUT")
					score=input("What was your score for this class? ")
			
			if(int(score) >= 90):
				points=4
			elif(int(score) >= 80 and int(score) <= 89):
				points=3
			elif(int(score) >= 70 and int(score) <= 79):
				points=2
			elif(int(score) >= 60 and int(score) <= 69):
				points=1
			else:
				points=0
			
			all_course_hours += int(cred_hr)
			all_course_point += (int(points)*int(cred_hr))

			course_limit += 1
			if (course_limit == 6 or all_course_hours >= 20):
				course_continue=False
			else:
				print("\nDo you have another course you wish to add?")
				course_add=input("ENTER y or n: ")
			
			input_valid = False
			while(input_valid==False and course_continue==True):
				if(course_add == 'y'):
					input_valid = True 
				elif(course_add == 'n'):
					input_valid = True 
					course_continue = False
				else:
					print("INPUT INVALID")
					print("Do you have another course you wish to add?")
					course_add=input("ENTER y or n: ")

		gpa = all_course_point/all_course_hours
		cumulative_gpa = "{:.2f}".format(gpa) 
		print()
		print(f"{self.f_name} {self.l_name}'s cumulative GPA is {cumulative_gpa}.")

def name_check(name):
	name_valid = False
	while(name_valid==False):
		if(name.isalpha()):
			name_valid=True
			return name
		else:
			name_valid=False
			print("INVALID INPUT")
			name=input("Please retype name: ")

print("Let's calculate your GPA.")
first_name=input("What is your first name? ")
name_check(first_name)
last_name=input("What is your last name? ")
name_check(last_name)
print()

s1=Student(first_name,last_name)
s1.initiation()
s1.gather_score()