#Anthony Nguyen, Assignment 1-3, 11/30/2024
#this program is part two of a two-part assignment
#to demonstrate the flow of a program, or in this case, the flow of a song

def bottles_song(num):
	#takes the inputted number as the argument
	#then uses it as the limit for a loop
	for x in reversed(range(num+1)):
		#initial iteration is 1 less, 1 is added to num to begin at the number
		#there's different lyrics for what number of bottle is left
		
		if (x != 0):#are there any bottles left
			if(x != 1):
				#lyrics for multiple bottles
				print(str(x) + " bottles of beer on the wall!")
				print(str(x) + " bottles of beeeeeeeeeeeeeer!")
				print("Take one down Pass it around!")
			else:
				#lyrics for one bottle
				print(str(x) + " bottle of beer on the wall!")
				print(str(x) + " bottle of beeeeeeeeeeeeeer!")
				print("Take one down Pass it around!")
				
				#check the num again for lyric change
			if ((x-1) != 0):#any bottles left
				if ((x-1) != 1):
					#many bottles left
					print(str(x-1) + " bottles of beer on the wall!\n")
				else:
					#one bottle left
					print(str(x-1) + " bottle of beer on the wall!\n")
			else: 
				#none left
				print("No more bottles of beer on the wall!")
		else:
			#lyrics for no bottles: print one more empty line then leave the function
			print()
			
	#after each run of the lyrics, move down to the next number in range 

#ask the user how many bottles
bottles=input("How many bottles of beer on the wall? ")

#check if user input is valid (number)
if (bottles.isnumeric() == False):
	print("INVALID INPUT")
else:#check if input is less than one
	if(int(bottles) < 1):
		print("INVALID INPUT")
	else:#initiate function if it's a number greater than 0
		print()
		bottles_song(int(bottles))
		#after the function, print the following:
		print("TIME TO BUY MORE BOTTLES OF BEER!")