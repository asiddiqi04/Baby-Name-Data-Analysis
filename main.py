#!/usr/bin/env python3
#Libraries
import os
import sys
import getopt
import pandas as pd

from functions.getAverageNameLength import getAverageNameLength
from functions.getMostPopularFirstChar import getMostPopularFirstChar
from functions.commonNamesOverTime import commonNames
from functions.averageNameRank import averageRank
from functions.totalNameFreq import totalNameFreq
from functions.getPopularNamesOfAlphabets import getPopularNamesOfAlphabets
from functions.getPopularNamesOfVowels import getPopularNamesOfVowels
from functions.ethnicNames import ethnicNames

#main function definition
def main():
  #formatting
  print("\n")
  print("Welcome to Team Cobra's Baby Name Analysis Application")
  print("This application has the capabilities of answering questions about the baby name data for 9 regions")
  print("and displaying a visual representation of the data.\n")
  #list of regions
  regions = ['Alberta','Austrailia','California', 'Ireland', 'New Brunswick','New Zealand', 'Nova Scotia', 'Ontario', 'Quebec']
  #while loop used to repeat error trap
  while True:
    #menu options
    print("Menu Options")
    print("y - Answer a question")
    print("x - Exit program")
    print("h - Help\n")
    #user choice
    charChoice = input("Enter choice: ")
    #conditional for y
    if charChoice.lower() == 'y':
      #while statement to repeat
      while True:
        try:
          print("Question Options:\n")
          print("1 - What is the average length of the baby names in a certain location, in a given year")
          print("2 - What are the 5 most common starting letters of baby names in a certain location, in a given year")
          print("3 - Has the number of common names between boys and girls increased over time?")
          print("4 - Total frequency of a given name in each region")
          print("5 - Find average rank of a given name in each region")
          print("6 - What is the most popular baby name that starts with each letter of the alphabet?")
          print("7 - What is the most popular baby name that starts with each vowel?")
          print("8 - View Ethnic Origin of Names Beta")
          print("9 - Back to Main Menu\n")

          userInput = int(input("Enter an integer value between 1 and 9: "))
          #conditional statements
          if userInput < 1 or userInput > 9:
            print("Invalid input. Please enter an integer value between 1 and 9.")
          elif userInput == 1:
            print("You selected Question 1.\n")
            getAverageNameLength()
          elif userInput == 2:
            print("You selected Question 2.\n")
            getMostPopularFirstChar()
          elif userInput == 3:
            print("You selected Question 3.\n")
            commonNames(regions)
          elif userInput == 4:
            print("You selected Question 4.\n")
            totalNameFreq()
          elif userInput == 5:
            print("You selected Question 5.\n")
            averageRank()
          elif userInput == 6:
            print("You selected Question 6.\n")
            getPopularNamesOfAlphabets()
          elif userInput == 7:
            print("You selected Question 7.\n")
            getPopularNamesOfVowels()
          elif userInput == 8:
            print("You selected Question 8.\n")
            ethnicNames()
          else:
            break
        #except used
        except ValueError:
          print("Invalid input. Please enter an integer value between 1 and 9.")
    #if user wants to exit the program
    elif charChoice.lower() == 'x':
      print("Program Ending")
      sys.exit()
    #if user wants to select help option
    elif charChoice.lower() == 'h':
      print("This is the help page:")
      print("1. What are the available regions?")
      print("2. How to use the program?")
      #while loop used to repeat code
      while True:
          try:
              #gathering user input
              helpChoice = int(input("Please enter your choice: "))
              if helpChoice < 1 or helpChoice > 2:
                  raise ValueError
              if helpChoice == 1:
                print("Available Regions: \n")
                i = 1
                for name in regions:
                  print(str(i) + ". " + name)
                  i += 1
                print("\n")
              elif helpChoice == 2:
                message = "\nThis program allows users to ask insightful questions about baby name data from 9 regions and provide some sort of quantitative answer.\nTo use the main menu you will be prompted to enter single characters that correspond to menu options. \nTo select a question you want to answer you will be prompted to enter an integer value that corresponds with the question. \nIf you are prompted to enter a name or region name then capitalization does not matter. \nSimilarly if you are prompted to enter a gender then the capitalization of \'Male\' or \'Female\' does not matter.\nIf you choose to visualize a function, close the tab that has the chart to continue using the program.\n"
                justifiedMessage = message.ljust(50)
                print(justifiedMessage)
              break
          except ValueError:
              print("Invalid input. Please Enter an Integer between (1-2)")
    #else statement
    else:
      print("Invalid Input: Enter (y or x or h)")
#main call
main()
