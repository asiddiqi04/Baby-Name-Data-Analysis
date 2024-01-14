#!/usr/bin/env python3
#
#   Description: 
#
#   This function gets the 5 most popular starting characters in a name and prints out their frequencies
#   if the user chooses to visualize this then it prints a pie chart of the top 15 characters
#
#   File Author(s): Ben Holbrook
#   Last Date Edited: April 6th / 2023
#

# Import Statement
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import string
from collections import Counter

from functions.getLocNames import getLocNames


def getMostPopularFirstChar():

    # Get a Valid Location from the user
    locList = getLocNames()
    while True:
        try:
            print("Enter the location you would like to search (or enter 0 for a list of all locations): ")
            location = input()
            location = location.lower()
        except ValueError:
            print("Invalid Input, Enter 0 for a List of Valid Locations")
        locationFound = 0
        # Checks to see if the entered location is in the list of valid locations
        for i in range(len(locList)):
            if location == locList[i].lower():
                locationFound += 1
                location = locList[i]
        if locationFound != 0:
            break
        else:
            # Prints the list of valid locations that can be entered
            if location == "0":
                print("Location Options are: ")
                for i in locList:
                    print(i)
            else:
                print("Invalid location (Enter 0 to see a list of all locations)")
                continue

    # Get a Gender from the user
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

    # Using the information obtained above we can get the filename that we will read the data from
    inputFileName = "region/" + location + "_" + gender + ".csv" 

    # get the list of all years used in the file
    allYears = []
    with open (inputFileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            allYears.append(int(row[2]))

    firstYear = allYears[0]
    lastYear = allYears[-1]  

    # Get a Year
    while True:
        try:
            print("Enter the year that you would like to search (File Contains " + str(firstYear) + " - " + str(lastYear) + " ): ")
            year = int(input())
        except ValueError:
            print("Invalid Input, Enter a year (Ex: 1980)")
            continue
        if int(year) < firstYear or int(year) > lastYear:
            print("Error, that year is invalid (File Contains " + str(firstYear) + " - " + str(lastYear) + " ): ")
            continue
        else:
            break
        
    # Initializes a list of all of the letters in the alphabet (uppercase)
    alphabet = list(string.ascii_uppercase)

    location = location.capitalize()
    gender = gender.capitalize()

    if (os.path.isfile(inputFileName)) == False:
        print("Error, File not found")
        return

    names = []
    freq = []

    # Open the csv file and get list of names and frequencies in the specified year
    with open (inputFileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[2] == str(year):
                names.append(row[0].upper())
                freq.append(int(row[3]))
    
    if len(names) == 0:
        print("No Reccords Found for " + str(year))
        return

    firstLetters = []

    # creates a list of all of the first letters of names in the year
    for i in range(len(names)):
        for j in range(freq[i]):
            firstLetters.append(names[i][0])

    # Counter counts the number of times that each first letter appears in the list and returns a list of the letter and then its frequency
    # ex: [[A, 232], [B, 453], [C, 893], ...]
    letterCounts = Counter(firstLetters)
    # most_common returns a list of the most common letters in the list
    allTopLetters = letterCounts.most_common(len(letterCounts))
    top15Letters = letterCounts.most_common(15)

    # gets the number of letters tied for first
    numLettersTiedForFirst = 0
    mostPopFreq = allTopLetters[0][1]
    for i in range(len(allTopLetters)):
        if allTopLetters[i][1] == mostPopFreq:
            numLettersTiedForFirst += 1

    # as long as there is not a 5 way tie for first then it prints the list otherwise it lets the user know there is a 6 way tie
    if numLettersTiedForFirst <= 5:
        top5Letters = letterCounts.most_common(5)
        for i in range(1,6):
            print(i, ": ", top5Letters[i-1][0], " [", top5Letters[i-1][1], "] occurences")
    else:
        print("There is a 6 way tie for first:")


    # Checks if the user would like to visualize
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

    # If they choose to visualize
    if choice.lower() == 'y':

        letterFreqs = [0]*26
    
        # Adds the frequencies for the top 15 letters for the visualization
        for i in range(len(top15Letters)):
            for j in range(len(alphabet)):
                if alphabet[j] == top15Letters[i][0]:
                    letterFreqs[j] = top15Letters[i][1]

        # Remove the other 9 letters from the list
        lettersToRemove = []

        for i in range(len(letterFreqs)):
            if letterFreqs[i] == 0:
                lettersToRemove.append(alphabet[i])

        for l in lettersToRemove:
            alphabet.remove(l)

        # Remove 0's from the list
        letterFreqs = [i for i in letterFreqs if i != 0]

        # Display a pie chart
        x = np.array(letterFreqs)
        plt.pie(x, labels = alphabet)
        plt.title("Popularity of Top 15 Letters")
        plt.show()