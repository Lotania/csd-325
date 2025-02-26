#Anthony Nguyen, Assignment 12
#This is a redo of Assignment 4 (originally, 0 points awarded)

import csv
from datetime import datetime

from matplotlib import pyplot as plt

#change 1: provide
print("HOW TO USE THIS PROGRAM")
print("Simply type the number for whether you want to see the graph for the high or low temperatures")
print("for Sitka in 2018. Once you view your chosen graph, click the red X to")
print("exit, then you can choose to view another graph or exit.\n")

print("Would you like to see the highs or lows, or leave?")
selection = input('1-HIGH, 2-LOW, or 3-EXIT ')

while(selection != '3'):
    #if the user wants to see the highs
    if(selection == '1'):
        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

            # Plot the high temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()
            
            print("Would you like to see the highs or lows, or leave?")
            selection = input('1-HIGH, 2-LOW, or 3-EXIT ')###added number options for clarity
    
    #if the user wants to see the lows
    elif(selection == '2'):
        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            
            # Get dates and low temperatures from this file.
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)
                
            # Plot the low temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')
        
            # Format plot.
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
        
            plt.show()
            
            print("Would you like to see the highs or lows, or leave?")
            selection = input('1-HIGH, 2-LOW, or 3-EXIT ')###added number options for clarity
            ###removed all 'cap_selection = selection.upper()' lines as they served no purpose
    
    #if the user no longer wants to continue
    elif(selection == '3'):
        break
    
    #if anything else is typed
    else:
        print("INVALID INPUT")
        print("Would you like to see the highs or lows, or leave?")
        selection = input('1-HIGH, 2-LOW, or 3-EXIT ') ###added number options for clarity

#print loop end message
print("\nThis ends the high/low program. BOODGYE.")

#flowcharts have been redone.
#Sitka_high_low_AVN will be separated into multiple pages to
#allow for clearer reading