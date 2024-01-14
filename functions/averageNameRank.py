#!/usr/bin/env python
#
#   Description: This Program takes the input of a gender and a name and prints the average rank of the
#                name in all the regions
#
#
#   File Author(s): Yousuf Mohiuddin
#   Last Date Edited: April 6/ 2023
#
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


def averageRank():

  #filenames
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
  #error trapping
  while True:
    gender = input("Enter The Gender of The Name (Female or Male): ")
    if gender.upper() == "FEMALE" or gender.upper(
    ) == 'MALE':  #checking if gender is female
      if (gender.upper()) == 'FEMALE':
        #error trapping
        while True:
          name = input("Please Enter a Name: ")
          if len(name) == 0:
            print("Name Must Have length greater than 0")
          elif not all(char.isalpha() or char == '-' or char == "'"
                       for char in name):
            print("Error, Invalid Input, Try Again")
          else:
            break
        if (len(name) != 0):
          name = name[0].upper() + name[1:].lower()
        totalAvgRanks = []
        locations = []
        #searching files
        NZF_name_Count = 0
        NZF_Avg_Rank = 0
        newZealand_Female_df = pd.read_csv(NewZealand_female_filename)
        for i in range(0, len(newZealand_Female_df)):
          if (newZealand_Female_df.loc[i, 'Name'].lower() == name.lower()):
            NZF_Avg_Rank += int(newZealand_Female_df.loc[i, 'Rank'])
            #increment
            NZF_name_Count += 1
        if (NZF_Avg_Rank != 0):
          locations.append("New Zealand")
          totalAvgRanks.append(NZF_Avg_Rank)
        #if dividing by 0 then print this statement
        if NZF_name_Count == 0:
          print("Average Rank of", name, "In", "New Zealand Female:", 0)
        else:
          print("Average Rank of", name, "In", "New Zealand Female:",
                int(NZF_Avg_Rank / NZF_name_Count))
        #searching files
        NBF_name_count = 0
        NBF_Avg_Rank = 0
        newBrunswick_Female_df = pd.read_csv(NewBrunswick_female_filename)
        for i in range(0, len(newBrunswick_Female_df)):
          if (newBrunswick_Female_df.loc[i, 'Name'].lower() == name.lower()):
            NBF_Avg_Rank += int(newZealand_Female_df.loc[i, 'Rank'])
            #increment
            NBF_name_count += 1
        if (NBF_Avg_Rank != 0):
          locations.append("New Brunswick")
          totalAvgRanks.append(NBF_Avg_Rank)
        if NBF_name_count == 0:
          print("Average Rank of", name, "In", "New Brunswick Female:", 0)
        else:
          print("Average Rank of", name, "In", "New Brunswick Female:",
                int(NBF_Avg_Rank / NBF_name_count))
        #searching files
        IRF_name_count = 0
        IRF_Avg_Rank = 0
        Ireland_Female_df = pd.read_csv(Ireland_female_filename)
        for i in range(0, len(Ireland_Female_df)):
          if (Ireland_Female_df.loc[i, 'Name'].lower() == name.lower()):
            IRF_Avg_Rank += int(Ireland_Female_df.loc[i, 'Rank'])
            #increment
            IRF_name_count += 1
        if (IRF_Avg_Rank != 0):
          locations.append("Ireland")
          totalAvgRanks.append(IRF_Avg_Rank)
        if IRF_name_count == 0:
          print("Average Rank of", name, "In", "Ireland Female:", 0)
        else:
          print("Average Rank of", name, "In", "Ireland Female:",
                int(IRF_Avg_Rank / IRF_name_count))
        #searching files
        NSF_name_count = 0
        NSF_Avg_Rank = 0
        NovaScotia_Female_df = pd.read_csv("region/novaScotia_female.csv")
        for i in range(0, len(NovaScotia_Female_df)):
          if (NovaScotia_Female_df.loc[i, 'Name'].lower() == name.lower()):
            NSF_Avg_Rank += int(NovaScotia_Female_df.loc[i, 'Rank'])
            #increment
            NSF_name_count += 1
        if (NSF_Avg_Rank != 0):
          locations.append("Nova Scotia")
          totalAvgRanks.append(NSF_Avg_Rank)
        if NSF_name_count == 0:
          print("Average Rank of", name, "In", "Nova Scotia Female:", 0)
        else:
          print("Average Rank of", name, "In", "Nova Scotia Female:",
                int(NSF_Avg_Rank / NSF_name_count))
        #searching files
        CAF_name_count = 0
        CAF_Avg_Rank = 0
        California_Female_df = pd.read_csv(California_female_filename)
        for i in range(0, len(California_Female_df)):
          if (California_Female_df.loc[i, 'Name'].lower() == name.lower()):
            CAF_Avg_Rank += int(California_Female_df.loc[i, 'Rank'])
            #increment
            CAF_name_count += 1
        if (CAF_Avg_Rank != 0):
          locations.append("California")
          totalAvgRanks.append(NSF_Avg_Rank)
        if CAF_name_count == 0:
          print("Average Rank of", name, "In", "California Female:", 0)
        else:
          print("Average Rank of", name, "In", "California Female:",
                int(CAF_Avg_Rank / CAF_name_count))
        #searching files
        ALF_name_count = 0
        ALF_Avg_Rank = 0
        Alberta_Female_df = pd.read_csv(Alberta_female_filename)
        for i in range(0, len(Alberta_Female_df)):
          if (str(Alberta_Female_df.loc[i, 'Name']).lower() == name.lower()):
            ALF_Avg_Rank += int(Alberta_Female_df.loc[i, 'Rank'])
            #increment
            ALF_name_count += 1
        if (ALF_Avg_Rank != 0):
          locations.append("Alberta")
          totalAvgRanks.append(NSF_Avg_Rank)
        if ALF_name_count == 0:
          print("Average Rank of", name, "In", "Alberta Female:", 0)
        else:
          print("Average Rank of", name, "In", "Alberta Female:",
                int(ALF_Avg_Rank / ALF_name_count))
        #searching files
        QBF_name_count = 0
        QBF_Avg_Rank = 0
        Quebec_Female_df = pd.read_csv(Quebec_female_filename)
        for i in range(0, len(Quebec_Female_df)):
          if (str(Quebec_Female_df.loc[i, 'Name']).lower() == name.lower()):
            QBF_Avg_Rank += int(Quebec_Female_df.loc[i, 'Rank'])
            #increment
            QBF_name_count += 1
        if (QBF_Avg_Rank != 0):
          locations.append("Quebec")
          totalAvgRanks.append(NSF_Avg_Rank)
        if QBF_name_count == 0:
          print("Average Rank of", name, "In", "Quebec Female:", 0)
        else:
          print("Average Rank of", name, "In", "Quebec Female:",
                int(QBF_Avg_Rank / QBF_name_count))
        #searching files
        ONF_name_count = 0
        ONF_Avg_Rank = 0
        Ontario_Female_df = pd.read_csv(Ontario_female_filename)
        for i in range(0, len(Ontario_Female_df)):
          if (str(Ontario_Female_df.loc[i, 'Name']).lower() == name.lower()):
            ONF_Avg_Rank += int(Ontario_Female_df.loc[i, 'Rank'])
            ONF_name_count += 1
        if (ONF_Avg_Rank != 0):
          locations.append("Ontario")
          totalAvgRanks.append(NSF_Avg_Rank)
        if ONF_name_count == 0:
          print("Average Rank of", name, "In", "Ontario Female:", 0)
        else:
          print("Average Rank of", name, "In", "Ontario Female:",
                int(ONF_Avg_Rank / ONF_name_count))
        #Austrailia Data
        AUS_name_count = 0
        AUS_Avg_Rank = 0
        austrailia_female_df = pd.read_csv(austrailia_female_filename)
        for i in range(0, len(austrailia_female_df)):
          if (str(austrailia_female_df.loc[i,
                                           'Name']).lower() == name.lower()):
            AUS_Avg_Rank += int(austrailia_female_df.loc[i, 'Rank'])
            AUS_name_count += 1
        if (AUS_Avg_Rank != 0):
          locations.append("Austrailia")
          totalAvgRanks.append(AUS_Avg_Rank)
        if AUS_name_count == 0:
          print("Average Rank of", name, "In", "Austrailia Female:", 0)
        else:
          print("Average Rank of", name, "In", "Austrailia Female:",
                int(AUS_Avg_Rank / AUS_name_count))
        #plotting the data
        #gathering user input
        choice = input(
          "Would you Like to see Visualization of This Data (Enter y if yes, Enter any key if no): "
        )
        if choice == 'y':
          if (len(locations) != 0 and len(totalAvgRanks) != 0):
            #plotting the data
            x = locations
            y = totalAvgRanks
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
          elif (len(locations) == 0 or len(totalAvgRanks) == 0):
            print("This Name Has No Data, No Visualization Possible")
      #if gender is Male
      elif (gender.upper()) == 'MALE':
        #error trapping
        while True:
          name = input("Please Enter a Name: ")
          if len(name) == 0:
            print("Name Must Have length greater than 0")
          elif not all(char.isalpha() or char == '-' or char == "'"
                       for char in name):
            print("Error, Invalid Input, Try Again")
          else:
            break
        if (len(name) != 0):
          name = name[0].upper() + name[1:].lower()
        locations = []
        totalAvgRanks = []
        #searching files
        NZM_name_Count = 0
        NZM_Avg_Rank = 0
        newZealand_male_df = pd.read_csv(NewZealand_male_filename)
        for i in range(0, len(newZealand_male_df)):
          if (newZealand_male_df.loc[i, 'Name'].lower() == name.lower()):
            NZM_Avg_Rank += int(newZealand_male_df.loc[i, 'Rank'])
            #increment
            NZM_name_Count += 1
        if (NZM_Avg_Rank != 0):
          locations.append("New Zealand")
          totalAvgRanks.append(NZM_Avg_Rank)
        if NZM_name_Count == 0:
          print("Average Rank of", name, "In", "New Zealand Male:", 0)
        else:
          print("Average Rank of", name, "In", "New Zealand Male:",
                int(NZM_Avg_Rank / NZM_name_Count))
        #searching files
        NBM_name_count = 0
        NBM_Avg_Rank = 0
        newBrunswick_male_df = pd.read_csv(NewBrunswick_male_filename)
        for i in range(0, len(newBrunswick_male_df)):
          if (newBrunswick_male_df.loc[i, 'Name'].lower() == name.lower()):
            NBM_Avg_Rank += int(newZealand_male_df.loc[i, 'Rank'])
            #increment
            NBM_name_count += 1
        if (NBM_Avg_Rank != 0):
          locations.append("New Brunswick")
          totalAvgRanks.append(NBM_Avg_Rank)
        if NBM_name_count == 0:
          print("Average Rank of", name, "In", "New Brunswick Male:", 0)
        else:
          print("Average Rank of", name, "In", "New Brunswick Male:",
                int(NBM_Avg_Rank / NBM_name_count))
        #searching files
        IRM_name_count = 0
        IRM_Avg_Rank = 0
        Ireland_male_df = pd.read_csv(Ireland_male_filename)
        for i in range(0, len(Ireland_male_df)):
          if (Ireland_male_df.loc[i, 'Name'].lower() == name.lower()):
            IRM_Avg_Rank += int(Ireland_male_df.loc[i, 'Rank'])
            #increment
            IRM_name_count += 1
        if (IRM_Avg_Rank != 0):
          locations.append("Ireland")
          totalAvgRanks.append(IRM_Avg_Rank)
        if IRM_name_count == 0:
          print("Average Rank of", name, "In", "Ireland Male:", 0)
        else:
          print("Average Rank of", name, "In", "Ireland Male:",
                int(IRM_Avg_Rank / IRM_name_count))
        #searching files
        NSM_name_count = 0
        NSM_Avg_Rank = 0
        NovaScotia_male_df = pd.read_csv("region/novaScotia_male.csv")
        for i in range(0, len(NovaScotia_male_df)):
          if (NovaScotia_male_df.loc[i, 'Name'].lower() == name.lower()):
            NSM_Avg_Rank += int(NovaScotia_male_df.loc[i, 'Rank'])
            #increment
            NSM_name_count += 1
        if (NSM_Avg_Rank != 0):
          locations.append("Nova Scotia")
          totalAvgRanks.append(NSM_Avg_Rank)
        if NSM_name_count == 0:
          print("Average Rank of", name, "In", "Nova Scotia Male:", 0)
        else:
          print("Average Rank of", name, "In", "Nova Scotia Female:",
                int(NSM_Avg_Rank / NSM_name_count))
        #searching files
        CAM_name_count = 0
        CAM_Avg_Rank = 0
        California_male_df = pd.read_csv(California_male_filename)
        for i in range(0, len(California_male_df)):
          if (California_male_df.loc[i, 'Name'].lower() == name.lower()):
            CAM_Avg_Rank += int(California_male_df.loc[i, 'Rank'])
            #increment
            CAM_name_count += 1
        if (CAM_Avg_Rank != 0):
          locations.append("California")
          totalAvgRanks.append(CAM_Avg_Rank)
        if CAM_name_count == 0:
          print("Average Rank of", name, "In", "California Male:", 0)
        else:
          print("Average Rank of", name, "In", "California Male:",
                int(CAM_Avg_Rank / CAM_name_count))
        #searching files
        ALM_name_count = 0
        ALM_Avg_Rank = 0
        Alberta_male_df = pd.read_csv(Alberta_male_filename)
        for i in range(0, len(Alberta_male_df)):
          if (str(Alberta_male_df.loc[i, 'Name']).lower() == name.lower()):
            ALM_Avg_Rank += int(Alberta_male_df.loc[i, 'Rank'])
            #increment
            ALM_name_count += 1
        if (ALM_Avg_Rank != 0):
          locations.append("Alberta")
          totalAvgRanks.append(ALM_Avg_Rank)
        if ALM_name_count == 0:
          print("Average Rank of", name, "In", "Alberta Male:", 0)
        else:
          print("Average Rank of", name, "In", "Alberta Male:",
                int(ALM_Avg_Rank / ALM_name_count))
        #searching files
        QBM_name_count = 0
        QBM_Avg_Rank = 0
        Quebec_male_df = pd.read_csv(Quebec_male_filename)
        for i in range(0, len(Quebec_male_df)):
          if (str(Quebec_male_df.loc[i, 'Name']).lower() == name.lower()):
            QBM_Avg_Rank += int(Quebec_male_df.loc[i, 'Rank'])
            #increment
            QBM_name_count += 1
        if (QBM_Avg_Rank != 0):
          locations.append("Quebec")
          totalAvgRanks.append(QBM_Avg_Rank)
        if QBM_name_count == 0:
          print("Average Rank of", name, "In", "Quebec Male:", 0)
        else:
          print("Average Rank of", name, "In", "Quebec Male:",
                int(QBM_Avg_Rank / QBM_name_count))
        #searching files
        ONM_name_count = 0
        ONM_Avg_Rank = 0
        Ontario_male_df = pd.read_csv(Ontario_male_filename)
        for i in range(0, len(Ontario_male_df)):
          if (str(Ontario_male_df.loc[i, 'Name']).lower() == name.lower()):
            ONM_Avg_Rank += int(Quebec_male_df.loc[i, 'Rank'])
            #increment
            ONM_name_count += 1
        if (ONM_Avg_Rank != 0):
          locations.append("Ontario")
          totalAvgRanks.append(ONM_Avg_Rank)
        if ONM_name_count == 0:
          print("Average Rank of", name, "In", "Ontario Male:", 0)
        else:
          print("Average Rank of", name, "In", "Ontario Male:",
                int(ONM_Avg_Rank / ONM_name_count))
        #Austrailia Data
        AUSM_name_count = 0
        AUSM_Avg_Rank = 0
        austrailia_male_df = pd.read_csv(austrailia_male_filename)
        for i in range(0, len(austrailia_male_df)):
          if (str(austrailia_male_df.loc[i, 'Name']).lower() == name.lower()):
            AUSM_Avg_Rank += int(austrailia_male_df.loc[i, 'Rank'])
            AUSM_name_count += 1
        if (AUSM_Avg_Rank != 0):
          locations.append("Austrailia")
          totalAvgRanks.append(AUSM_Avg_Rank)
        if AUSM_name_count == 0:
          print("Average Rank of", name, "In", "Austrailia Male:", 0)
        else:
          print("Average Rank of", name, "In", "Austrailia Male:",
                int(AUSM_Avg_Rank / AUSM_name_count))
        #plotting the data
        #gathering user input
        choice = input(
          "Would you Like to see Visualization of This Data (Enter y if yes, Enter any key if no): "
        )
        if choice == 'y':
          if (len(locations) != 0 and len(totalAvgRanks) != 0):
            #plotting the data
            x = locations
            y = totalAvgRanks
            # plotting the points
            plt.plot(x, y)
            # labelling x and y axis
            plt.xlabel('Locations')
            plt.ylabel('Average Rank')
            #giving title to graph
            plt.title("Average Rank of " + name + " Across Locations")
            #changing font size
            plt.xticks(fontsize=7.5)
            # displaying the graph
            plt.show()
          elif (len(locations) == 0 or len(totalAvgRanks) == 0):
            print("This Name Has No Data, No Visualization Possible")
      break
    else:
      #output if there is an error
      print("Not a Gender Try Again")
