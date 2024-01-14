#!/usr/bin/env python3

#
#   Description: This program is used to process the 2 ireland csv files downloaded from:
#   https://www.cso.ie/en/releasesandpublications/ep/p-ibn/irishbabiesnames2022/data/
#
#   Note: These files only contain the names that appear at least 3 times, otherwise the frequency is blank
#
#   The result will be 2 CSV Files, 1 for each gender
#
#   File Author(s): Ben Holbrook
#   Last Date Edited: March 13 / 2023
#


# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main ( argv ):

    if len(argv) < 3:
        print("Usage: ./irelandProcessing -m <maleFileName> -f <femaleFileName> ")
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt (argv, "m:f:", ["maleFileName=", "femaleFileName="] )
    except getopt.GetoptError:
        print("Usage: ./irelandProcessing -m <maleFileName> -f <femaleFileName> ")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ./irelandProcessing -m <maleFileName> -f <femaleFileName> ")
            sys.exit()
        elif opt in ( "-m", "--maleFileName"):
            maleInputFileName = arg
        elif opt in ( "-f", "--femaleFileName"):
            femaleInputFileName = arg

    male_outputFileName = "ireland_male.csv"
    female_outputFileName = "ireland_female.csv"



    # decare a list for each row in the CSV File
    female_names = []
    female_frequencies = []
    female_ranks = []
    female_years = []
    female_total = 0

    male_names = []
    male_frequencies = []
    male_ranks = []
    male_years = []
    male_total = 0


    with open (maleInputFileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[0] == "Boys Names in Ireland with 3 or More Occurrences":
                if row[4] != "":
                    name = row[2].strip()
                    male_names.append(name)
                    male_years.append(int(row[1]))
                    male_frequencies.append(int(row[4]))
                    male_total = male_total + 1


    with open (femaleInputFileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[0] == "Girls Names in Ireland with 3 or More Occurrences":
                if row[4] != "":
                    name = row[2].strip()
                    female_names.append(name)
                    female_years.append(int(row[1]))
                    female_frequencies.append(int(row[4]))
                    female_total = female_total + 1

    if male_total > 0:
        male_dataSet = {'Name':male_names, 'Year':male_years, 'Freq':male_frequencies}
        male_dataFrame = pd.DataFrame(male_dataSet)
        male_dataFrame.sort_values(by=['Year', 'Freq', 'Name'], axis = 0, ascending=[True, False, True], inplace=True)


        male_yearCol = male_dataFrame['Year']
        male_freqCol = male_dataFrame['Freq']
        
        lastYear = 1964
        counter = 0
        for i in range(len(male_yearCol.values)): # for each year in the year column
            if male_yearCol.values[i] != lastYear: # if there is a year change we reset the rank counter back to 0
                counter = 0
            counter = counter + 1 # add a value to the rank
            lastYear = male_yearCol.values[i]

            if counter != 1:
                if male_freqCol.values[i] == male_freqCol.values[i - 1]:
                    j = 0
                    while male_freqCol.values[i] == male_freqCol.values[i - j]:
                        j = j + 1
                    temp_rank_index = len(male_ranks)
                    male_ranks.append(male_ranks[temp_rank_index - 1])
                else:
                    male_ranks.append(counter)
            else:
                male_ranks.append(counter)


        male_dataFrame = male_dataFrame.assign(Rank=male_ranks)

        #Reorder the cols
        male_dataFrame = male_dataFrame.iloc[:, [0,3,1,2]]

        male_dataFrame.to_csv(male_outputFileName, sep=',', index=False, encoding='utf-8')

    if female_total > 0:
        female_dataSet = {'Name':female_names, 'Year':female_years, 'Freq':female_frequencies}
        female_dataFrame = pd.DataFrame(female_dataSet)
        female_dataFrame.sort_values(by=['Year', 'Freq', 'Name'], axis = 0, ascending=[True, False, True], inplace=True)

        female_yearCol = female_dataFrame['Year']
        female_freqCol = female_dataFrame['Freq']
        
        lastYear = female_yearCol[0]
        counter = 0
        for i in range(len(female_yearCol.values)): # for each year in the year column
            if female_yearCol.values[i] != lastYear: # if there is a year change we reset the rank counter back to 0
                counter = 0
            counter = counter + 1 # add a value to the rank (ensures that there is no rank 0)
            lastYear = female_yearCol.values[i]

            if counter != 1:
                if female_freqCol.values[i] == female_freqCol.values[i - 1]:
                    numberOfNamesTied = 0
                    while female_freqCol.values[i] == female_freqCol.values[i - numberOfNamesTied]:
                        numberOfNamesTied = numberOfNamesTied + 1
                    temp_rank_index = len(female_ranks)
                    female_ranks.append(female_ranks[temp_rank_index - 1])
                else:
                    female_ranks.append(counter)
            else:
                female_ranks.append(counter)


        female_dataFrame = female_dataFrame.assign(Rank=female_ranks)

        #Reorder the cols
        female_dataFrame = female_dataFrame.iloc[:, [0,3,1,2]]

        female_dataFrame.to_csv(female_outputFileName, sep=',', index=False, encoding='utf-8')


if __name__ == "__main__":
    main ( sys.argv[1:] )
