#!/usr/bin/env python3

#
#   Description:
#
#   This function gets the average name length for a certain gender in a given year, it then gives
#   the option to visualize that data for all the years that the file contains
#
#   File Author(s): Ben Holbrook
#   Last Date Edited: April 6th / 2023
#

# Import Statements
import os
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np

from functions.getLocNames import getLocNames

# Note: gender must be formatted to either "male" or "female" for this to work and same with location, it must be the exact
#       name that the start of the data file uses or else this function will not open the correct file


def getAverageNameLength():

  year = "get from user"

  # Get a Valid Location from user, while ensuring correct input
  locList = getLocNames()
  while True:
    try:
      print(
        "Enter the location you would like to search (or enter 0 for a list of all locations): "
      )
      location = input()
      location = location.lower()
    except ValueError:
      print("Invalid Input, Enter 0 for a List of Valid Locations")
    locationFound = 0
    # Checks the list of all valid locations to make sure that they entered a location that we have data for
    for i in range(len(locList)):
      if location == locList[i].lower():
        locationFound += 1
        location = locList[i]
    if locationFound != 0:
      break
    else:
      # If a 0 is entered, print a list of all of the location options
      if location == "0":
        print("\nLocation Options are: ")
        for i in locList:
          print(i)
        print(" ")
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
    # Keep asking for input until gender entered is male or female
    if gender == "male" or gender == "female":
      break
    else:
      print("Invalid Input, try again")
      continue

  # useing the information above get the file name to open
  inputFileName = "region/" + location + "_" + gender + ".csv"

  # get the list of all years used in the file
  allYears = []
  with open(inputFileName) as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
      allYears.append(int(row[2]))

  # First year will be the first element in the year column of every file
  firstYear = allYears[0]
  # Last year will always be the last element in the year column
  lastYear = allYears[-1]

  # Get a Year
  while True:
    try:
      print("Enter the year that you would like to search (File Contains " +
            str(firstYear) + " - " + str(lastYear) + " ): ")
      year = int(input())
    except ValueError:
      print("Invalid Input, Enter a year (File Contains " + str(firstYear) +
            " - " + str(lastYear) + " )")
      continue
    # Check to make sure that the year is within the range contained in the file
    if int(year) < firstYear or int(year) > lastYear:
      print("Error, that year is invalid (File Contains " + str(firstYear) +
            " - " + str(lastYear) + " ): ")
      continue
    else:
      break
  # Capitalize the names for printing
  location = location.capitalize()
  gender = gender.capitalize()

  if (os.path.isfile(inputFileName)) == False:
    print("Error, File not found")
    return

  names = []
  freq = []
  years = []

  # Get Open the files and read in names, frequencies and years
  with open(inputFileName) as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
      names.append(row[0])
      freq.append(int(row[3]))
      years.append(int(row[2]))

  # see how many records are in that year
  counter = 0
  for i in range(len(years)):
    if str(years[i]) == str(year):
      counter += 1

  if counter == len(years):
    print("There were no records found for ", year)

  # Calculates the average name length
  numOfChars = 0
  numOfWords = 0
  for i in range(len(names)):
    if str(years[i]) == str(year):
      # for each name, multiply its length by its frequency to get total number of chars
      numOfChars += len(names[i]) * freq[i]
      # for each word increment numOfWords to get total number of words
      numOfWords += freq[i]

  averageNameLength = numOfChars / numOfWords

  print("Average Name Length in " + str(year) + " is: " +
        str(round(averageNameLength, 2)))

  # Ask if they would like to visualize
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

      # if they choose to visualize
  if choice.lower() == 'y':
    firstYear = years[0]
    lastYear = years[-1]

    allYears = []
    avNameLengths = []

    # same as the above calcualtion for one year, but does it for all years in the file
    for i in range(firstYear, lastYear + 1):
      allYears.append(i)
      numOfWords = 0
      numOfChars = 0
      for j in range(len(years)):
        if years[j] == i:
          numOfChars += len(names[j]) * freq[j]
          numOfWords += freq[j]

      if numOfWords == 0:
        allYears.remove(i)
      else:
        avNameLengths.append(numOfChars / numOfWords)

    # Plot the data on a graph
    x = np.array(allYears)
    y = np.array(avNameLengths)

    plt.plot(x, y)
    plt.xlabel("Years")
    plt.ylabel("Average Name Length")
    plt.title("Average Name Length in " + location + " for " + gender +
              "s from " + str(firstYear) + " to " + str(lastYear))
    plt.show()
