#!/usr/bin/env python
#
#   Description: This Function Asks the user for an input of a gender, then asks them to enter the name,
#                it will then traverse through the dataframes and output the data
#
#
#
#   File Author(s): Yousuf Mohiuddin
#   Last Date Edited: April 6/ 2023
#
#import statements
import os
import sys
import getopt
import csv
import pandas as pd
import glob
from itertools import accumulate
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt


#function definitions
def totalNameFreq():
  #fileNames
  NewZealand_female_filename = "region/newZealand_female.csv"
  NewZealand_male_filename = "region/newZealand_male.csv"
  NewBrunswick_female_filename = "region/newBrunswick_female.csv"
  NewBrunswick_male_filename = "region/newBrunswick_male.csv"
  Ireland_female_filename = "region/ireland_female.csv"
  Ireland_male_filename = "region/ireland_male.csv"
  NovaScotia_female_filename = "region/novaScotia_female.csv"
  NovaScotia_male_filename = "region/novaScotia_male.csv"
  California_female_filename = "region/california_female.csv"
  California_male_filename = "region/california_male.csv"
  Alberta_female_filename = "region/alberta_female.csv"
  Alberta_male_filename = "region/alberta_male.csv"
  Quebec_female_filename = "region/quebec_female.csv"
  Quebec_male_filename = "region/quebec_male.csv"
  Ontario_female_filename = "region/ontario_female.csv"
  Ontario_male_filename = "region/ontario_male.csv"
  austrailia_female_filename = "region/australia_female.csv"
  austrailia_male_filename = "region/australia_male.csv"
  #Gathering  User inputs
  while True:
    gender = input("Enter The Gender of The Name (Female or Male): ")
    if gender.upper() == "FEMALE" or gender.upper(
    ) == 'MALE':  #checking if gender is female or male
      if gender.upper() == 'FEMALE':
        #error trapping
        while True:
          name = input("Please Enter a Name: ")
          #will repeat if empty string is inputted
          if len(name) == 0:
            print("Name Must Have length greater than 0")
          #will repeat if name has invalid characters
          elif not all(char.isalpha() or char == '-' or char == "'"
                       for char in name):
            print("Error, Invalid Input, Try Again")
          else:
            break
        if (len(name) != 0):
          name = name[0].upper() + name[1:].lower()
        #declared list
        locations = []
        totalFreq = []
        #searching files
        newZealand_Female_Freq = 0
        newZealand_Female_df = pd.read_csv(NewZealand_female_filename)
        for i in range(0, len(newZealand_Female_df)):
          if (newZealand_Female_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            newZealand_Female_Freq += int(newZealand_Female_df.loc[i, 'Freq'])
        if (newZealand_Female_Freq != 0):
          locations.append("New Zealand")
          totalFreq.append(newZealand_Female_Freq)
        print("Total Frequency of", name, "In", "New Zealand Female:",
              newZealand_Female_Freq)
        #searching the files
        newBrunswick_female_Freq = 0
        newBrunswick_female_df = pd.read_csv(NewBrunswick_female_filename)
        for i in range(0, len(newBrunswick_female_df)):
          if (newBrunswick_female_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            newBrunswick_female_Freq += int(newBrunswick_female_df.loc[i,
                                                                       'Freq'])
        if (newBrunswick_female_Freq != 0):
          locations.append("New Brunswick")
          totalFreq.append(newBrunswick_female_Freq)
        print("Total Frequency of", name, "In", "New Brunswick Female:",
              newBrunswick_female_Freq)
        #searching files
        Ireland_female_Freq = 0
        Ireland_female_df = pd.read_csv(Ireland_female_filename)
        for i in range(0, len(Ireland_female_df)):
          if (Ireland_female_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            Ireland_female_Freq += int(Ireland_female_df.loc[i, 'Freq'])
        if (Ireland_female_Freq != 0):
          locations.append("Ireland")
          totalFreq.append(Ireland_female_Freq)
        print("Total Frequency of", name, "In", "Ireland Female:",
              Ireland_female_Freq)
        #searching files
        NovaScotia_female_Freq = 0
        NovaScotia_female_df = pd.read_csv(NovaScotia_female_filename)
        for i in range(0, len(NovaScotia_female_df)):
          if (NovaScotia_female_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            NovaScotia_female_Freq += int(NovaScotia_female_df.loc[i, 'Freq'])
        if (NovaScotia_female_Freq != 0):
          locations.append("Nova Scotia")
          totalFreq.append(NovaScotia_female_Freq)
        print("Total Frequency of", name, "In", "Nova Scotia Female:",
              NovaScotia_female_Freq)
        #searching files
        California_female_Freq = 0
        California_female_df = pd.read_csv(California_female_filename)
        for i in range(0, len(California_female_df)):
          if (California_female_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            California_female_Freq += int(California_female_df.loc[i, 'Freq'])
        if (California_female_Freq != 0):
          locations.append("California")
          totalFreq.append(California_female_Freq)
        print("Total Frequency of", name, "In", "California Female:",
              California_female_Freq)
        #searching files
        Alberta_female_Freq = 0
        Alberta_female_df = pd.read_csv(Alberta_female_filename)
        for i in range(0, len(Alberta_female_df)):
          if (str(Alberta_female_df.loc[i,
                                        'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Alberta_female_Freq += int(Alberta_female_df.loc[i, 'Freq'])
        if (Alberta_female_Freq != 0):
          locations.append("Alberta")
          totalFreq.append(Alberta_female_Freq)
        print("Total Frequency of", name, "In", "Alberta Female:",
              Alberta_female_Freq)
        #searching files
        Quebec_female_Freq = 0
        Quebec_female_df = pd.read_csv(Quebec_female_filename)
        for i in range(0, len(Quebec_female_df)):
          if (str(Quebec_female_df.loc[i,
                                       'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Quebec_female_Freq += int(Quebec_female_df.loc[i, 'Freq'])
        if (Quebec_female_Freq != 0):
          locations.append("Quebec")
          totalFreq.append(Quebec_female_Freq)
        print("Total Frequency of", name, "In", "Quebec Female:",
              Quebec_female_Freq)
        #searching files
        Ontario_female_Freq = 0
        Ontario_female_df = pd.read_csv(Ontario_female_filename)
        for i in range(0, len(Ontario_female_df)):
          if (str(Ontario_female_df.loc[i,
                                        'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Ontario_female_Freq += int(Ontario_female_df.loc[i, 'Freq'])
        if (Ontario_female_Freq != 0):
          locations.append("Ontario")
          totalFreq.append(Ontario_female_Freq)
        print("Total Frequency of", name, "In", "Ontario Female:",
              Ontario_female_Freq)
        #Austrailia Files
        AUS_female_Freq = 0
        Austrailia_female_df = pd.read_csv(austrailia_female_filename)
        for i in range(0, len(Austrailia_female_df)):
          if (str(
              Austrailia_female_df.loc[i,
                                       'Name']).lower() == str(name).lower()):
            #total freq being calculated
            AUS_female_Freq += int(Austrailia_female_df.loc[i, 'Freq'])
        if (AUS_female_Freq != 0):
          locations.append("Austrailia")
          totalFreq.append(AUS_female_Freq)
        print("Total Frequency of", name, "In", "Austrailia Female:",
              AUS_female_Freq)

        choice = input(
          "Would you Like to see Visualization of This Data (Enter y if yes, Enter any key if no): "
        )
        if choice.lower() == 'y':
          if (len(locations) != 0 and len(totalFreq) != 0):
            #plotting the data
            x = locations
            y = totalFreq
            # plotting the points
            plt.plot(x, y)
            # labelling x and y axis
            plt.xlabel('Locations')
            plt.ylabel('Total Frequency')
            #giving title to graph
            plt.title("Total Frequency of " + name + " Across Locations")
            #changing font size
            plt.xticks(fontsize=7.5)
            # displaying the graph
            plt.show()
          elif (len(locations) == 0 or len(totalFreq) == 0):
            print("This Name Has No Data, No Visualization Possible")

      #if gender is male
      elif gender.upper() == "MALE":
        while True:
          name = input("Please Enter a Name: ")
          if len(name) == 0:
            print("Name Must Have length greater than 0")
          #will repeat if name has invalid characters
          elif not all(char.isalpha() or char == '-' or char == "'"
                       for char in name):
            print("Error, Invalid Input, Try Again")
          else:
            break
        if (len(name) != 0):
          name = name[0].upper() + name[1:].lower()
        totalNameFreq = []
        locations = []
        newZealand_male_Freq = 0
        newZealand_male_df = pd.read_csv(NewZealand_male_filename)
        for i in range(0, len(newZealand_male_df)):
          if (newZealand_male_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            newZealand_male_Freq += int(newZealand_male_df.loc[i, 'Freq'])
        if (newZealand_male_Freq != 0):
          locations.append("New Zealand")
          totalNameFreq.append(newZealand_male_Freq)
        print("Total Frequency of", name, "In", "New Zealand Male:",
              newZealand_male_Freq)
        #searching files
        newBrunswick_male_Freq = 0
        newBrunswick_male_df = pd.read_csv(NewBrunswick_male_filename)
        for i in range(0, len(newBrunswick_male_df)):
          if (newBrunswick_male_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            newBrunswick_male_Freq += int(newBrunswick_male_df.loc[i, 'Freq'])
        if (newBrunswick_male_Freq != 0):
          locations.append("New Brunswick")
          totalNameFreq.append(newZealand_male_Freq)
        print("Total Frequency of", name, "In", "New Brunswick Male:",
              newBrunswick_male_Freq)
        #searching files
        Ireland_male_Freq = 0
        Ireland_male_df = pd.read_csv(Ireland_male_filename)
        for i in range(0, len(Ireland_male_df)):
          if (Ireland_male_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            Ireland_male_Freq += int(Ireland_male_df.loc[i, 'Freq'])
        if (Ireland_male_Freq != 0):
          locations.append("Ireland")
          totalNameFreq.append(Ireland_male_Freq)
        print("Total Frequency of", name, "In", "Ireland Male:",
              Ireland_male_Freq)
        #searching files
        California_male_Freq = 0
        California_male_df = pd.read_csv(California_male_filename)
        for i in range(0, len(California_male_df)):
          if (California_male_df.loc[i, 'Name'].lower() == name.lower()):
            #total freq being calculated
            California_male_Freq += int(California_male_df.loc[i, 'Freq'])
        if (California_male_Freq != 0):
          locations.append("California")
          totalNameFreq.append(California_male_Freq)
        print("Total Frequency of", name, "In", "California Male:",
              California_male_Freq)
        #searching files
        Alberta_male_Freq = 0
        Alberta_male_df = pd.read_csv(Alberta_male_filename)
        for i in range(0, len(Alberta_male_df)):
          if (str(Alberta_male_df.loc[i,
                                      'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Alberta_male_Freq += int(Alberta_male_df.loc[i, 'Freq'])
        if (Alberta_male_Freq != 0):
          locations.append("Alberta")
          totalNameFreq.append(Alberta_male_Freq)
        print("Total Frequency of", name, "In", "Alberta Male:",
              Alberta_male_Freq)
        #searching files
        Quebec_male_Freq = 0
        Quebec_male_df = pd.read_csv(Quebec_male_filename)
        for i in range(0, len(Quebec_male_df)):
          if (str(Quebec_male_df.loc[i, 'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Quebec_male_Freq += int(Quebec_male_df.loc[i, 'Freq'])
        if (Quebec_male_Freq != 0):
          locations.append("Quebec")
          totalNameFreq.append(Quebec_male_Freq)
        print("Total Frequency of", name, "In", "Quebec Male:",
              Quebec_male_Freq)
        #searching files
        Ontario_male_Freq = 0
        Ontario_male_df = pd.read_csv(Ontario_male_filename)
        for i in range(0, len(Ontario_male_df)):
          if (str(Ontario_male_df.loc[i,
                                      'Name']).lower() == str(name).lower()):
            #total freq being calculated
            Ontario_male_Freq += int(Ontario_male_df.loc[i, 'Freq'])
        if (Ontario_male_Freq != 0):
          locations.append("Ontario")
          totalNameFreq.append(Ontario_male_Freq)
        print("Total Frequency of", name, "In", "Ontario Male:",
              Ontario_male_Freq)
        #Austrailia Files
        AUS_male_Freq = 0
        Austrailia_male_df = pd.read_csv(austrailia_male_filename)
        for i in range(0, len(Austrailia_male_df)):
          if (str(
              Austrailia_male_df.loc[i, 'Name']).lower() == str(name).lower()):
            #total freq being calculated
            AUS_male_Freq += int(Austrailia_male_df.loc[i, 'Freq'])
        if (AUS_male_Freq != 0):
          locations.append("Austrailia")
          totalNameFreq.append(AUS_male_Freq)
        print("Total Frequency of", name, "In", "Austrailia Male:",
              AUS_male_Freq)
        #plotting the data
        #gathering user input
        choice = input(
          "Would you Like to see Visualization of This Data (Enter y if yes, Enter any key if no): "
        )
        if choice.lower() == 'y':
          if (len(locations) != 0 and len(totalNameFreq) != 0):
            #plotting the data
            x = locations
            y = totalNameFreq
            # plotting the points
            plt.plot(x, y)
            # labelling x and y axis
            plt.xlabel('Locations')
            plt.ylabel('Total Frequency')
            #giving title to graph
            plt.title("Total Frequency of " + name + " Across Locations")
            #changing font size
            plt.xticks(fontsize=7.5)
            # displaying the graph
            plt.show()
          elif (len(locations) == 0 or len(totalNameFreq) == 0):
            print("This Name Has No Data, No Visualization Possible")
      break
    #error trap
    else:
      print("Not a Gender Try Again")
