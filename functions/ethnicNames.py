#!/usr/bin/env python3

#
#   Description: 
#
#   This program is used to find and plot the ethnic origins of the top 25 names in 
#   a given year
#
#   File Author(s): Ben Holbrook
#   Last Date Edited: April 6th / 2023
#

# Import statements
import os
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np


def ethnicNames():
    
    # hardcoded the filename since it is the only file that could be used for this function
    fileName = "region/namsor_name-origin_california_male_last19y.csv"

    # prints disclaimer
    print("\nThis is a demo representation of analysing the ethinc origin of popular names in a region\n")
    print("** Disclaimer: The information below is based off the top 25 names in the given year. Due to those")
    print("limitations this data can not be used as an accurate representation of the general population **\n")

    names = []
    freq = []
    years = []
    regions = []
    
    listOfRegions = []
    freqOfRegions = []

    # open the file and read names, frequencies, years and regions into lists
    with open (fileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
                names.append(row[0])
                freq.append(int(row[3]))
                years.append(int(row[2]))
                regions.append(row[5])


    # Get a list of all of the regions that have at least one representative name
    for i in regions:
        regionFound = False
        for j in listOfRegions:
            if i == j:
                regionFound = True
        if regionFound == False:
            listOfRegions.append(i)


    lenRegions = len(listOfRegions)
    freqOfRegions = [0] * lenRegions


    # Get a Year

    firstYear = years[0]
    lastYear = years[-1]

    while True:
        try:
            print("Enter the year that you would like to search (File Contains " + str(firstYear) + " - " + str(lastYear) + " ): ")
            yearInput = int(input())
        except ValueError:
            print("Invalid Input, Enter a year (File Contains " + str(firstYear) + " - " + str(lastYear) + ")\n")
            continue
        # Checks to make sure that the year is contained in the file
        if int(yearInput) < firstYear or int(yearInput) > lastYear:
            print("Error, that year is invalid (File Contains " + str(firstYear) + " - " + str(lastYear) + ")\n")
            continue
        else:
            break
        
    # Updates the list freqOfRegions with the frequency that each region has a name in the rankings
    for i in range(len(years)):
        if years[i] == yearInput:
            for j in range(len(listOfRegions)):
                if regions[i] == listOfRegions[j]:
                    freqOfRegions[j] += 1


    # Prints the results for the user
    print("\nResults:\n")
    for i in range(len(listOfRegions)):
        print(listOfRegions[i] + " : "+ str(freqOfRegions[i]) + " occurances in the top 25")
    print(" ")

    # Gives the user the option to visualize this info
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

    
    if choice == 'Y' or choice == 'y':

        # Remove all regions from the list that have 0 occurances
        placesToRemove = []

        for i in range(len(freqOfRegions)):
            if freqOfRegions[i] == 0:
                placesToRemove.append(listOfRegions[i])

        # removes all 0's from the frequency list
        freqOfRegions = [i for i in freqOfRegions if i != 0]

        for i in range(len(placesToRemove)):
            listOfRegions.remove(placesToRemove[i])
        
        # Plot the data in a pie chart
        y = np.array(freqOfRegions)
        plt.pie(y, labels = listOfRegions)
        plt.show() 


