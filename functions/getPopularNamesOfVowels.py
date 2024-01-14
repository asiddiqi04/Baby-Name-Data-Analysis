#!/usr/bin/env python3

# Description:
#
# This function gets the most popular baby name that starts with each vowel
#
# File Author : Megan D Costa
# Last Date Edited : April 9 2023
#


import os
import pandas as pd


import matplotlib.pyplot as plt
import numpy as np

from functions.getLocNames import getLocNames
from functions.returnName import returnName

def getPopularNamesOfVowels():
  

    # Get a Valid Location
    locList = getLocNames()
    while True:
        try:
            print("Enter the location you would like to search (or enter 0 for a list of all locations): ")
            location = input()
            location = location.lower()
        except ValueError:
            print("Invalid Input, Enter 0 for a List of Valid Locations")
        locationFound = 0
        for i in range(len(locList)):
            if location == locList[i].lower():
                locationFound += 1
                location = locList[i]
        if locationFound != 0:
            break
        else:
            if location == "0":
                print("\nLocation Options are: ")
                for i in locList:
                    print(i)
                print(" ")
            else:
                print("Invalid location (Enter 0 to see a list of all locations)")
            continue


    # Get a Gender
    while True:
        try:
            print("Enter a Gender (Male or Female):")
            gender = str(input())
            gender = gender.lower()
        except ValueError:
            print("Invalid Input, Enter Male or Female")
        if gender == "male" or gender == "female":
            break
        else:
            print("Invalid Input, try again")
            continue


    
    inputFileName = "region/" + location + "_" + gender + ".csv" 

    location = location.capitalize ()
    gender = gender.capitalize () 

    if (os.path.isfile(inputFileName)) == False:
        print("Error, File not found")
        return

     # Load the data from the CSV file
    df = pd.read_csv(inputFileName)

    # Drop any rows with missing values in the 'Name' column
    df = df.dropna(subset=['Name'])
    vowel_names = []
    vowel_freqs = []

    # Loop over each letter of the alphabet
    for letter in 'AEIOU':
        # Filter the data to only include names that start with the current letter
        df_letter = df[df['Name'].str.startswith(letter)]

        # Find the name with the highest frequency
        if not df_letter.empty:
            max_freq = df_letter['Freq'].max()
            max_name = df_letter.loc[df_letter['Freq'] == max_freq, 'Name'].iloc[0]
            
            vowel_names.append(max_name)
            vowel_freqs.append(max_freq)
            newMaxName = returnName ( max_name ) 
            # Print the result
            print(f'{letter}: {newMaxName} ({max_freq})')

    print()

    while True:
        try:
            choice = str(input("Would you like to visualize it? (Y or N):"))
        except ValueError:
            print("Invalid Choice, enter Y or N to contine: ")
            continue

        if choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n':
            print("Invalid Choice, enter Y or N to contine: ")
            continue
        else:
            break

    if choice.lower() == 'y' :
        fig, ax = plt.subplots()
        ax.bar(vowel_names, vowel_freqs)
        ax.set_xlabel('Name')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Most Popular Names starting with Each Vowel in {location} ({gender})')
        plt.show()
