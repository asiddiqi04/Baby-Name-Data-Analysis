#!/usr/bin/env python3

#
#   Description: This program is used to process the albera csv file downloaded from:
#   https://open.alberta.ca/opendata/frequency-and-ranking-of-baby-names-by-year-and-gender
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

    if len(argv) < 2:
        print("Usage: ./albertaProcessing -i <fileName>")
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt (argv, "i:", ["input="] )
    except getopt.GetoptError:
        print("Usage: ./albertaProcessing -i <fileName>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ./albertaProcessing -i <fileName>")
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg

    male_outputFileName = "alberta_male.csv"
    female_outputFileName = "alberta_female.csv"




    # decare a list for each row in the CSV File
    female_names = []
    female_frequencies = []
    female_ranks = []
    female_years = []

    male_names = []
    male_frequencies = []
    male_ranks = []
    male_years = []



    with open (inputFileName) as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[3] == "Boy":
                male_tempName = row[1].strip()
                male_names.append(male_tempName.upper())
                male_ranks.append(int(row[0]))
                male_years.append(int(row[4]))
                male_frequencies.append(int(row[2]))
                male_infoRead = True
            elif row[3] == "Girl":
                female_tempName = row[1].strip()
                female_names.append(female_tempName.upper())
                female_ranks.append(int(row[0]))
                female_years.append(int(row[4]))
                female_frequencies.append(int(row[2]))
                female_infoRead = True
            else:
                print("Error, Invalid Row Found. Check format of input file")
        


        if male_infoRead:
            male_dataSet = {'Name':male_names, 'Rank':male_ranks, 'Year':male_years, 'Freq':male_frequencies}
            male_dataFrame = pd.DataFrame(male_dataSet)

            # To account for duplciated entries found in testing

            duplicateDF = male_dataFrame.duplicated(subset=['Year', 'Name'])
            duplicateIndexes = []
            freq_column = male_dataFrame['Freq']

            for i in range(len(duplicateDF)):
                if duplicateDF[i] == True:
                    offset = 1
                    while(male_dataFrame.iloc[i]['Name'] != male_dataFrame.iloc[i - offset]['Name']): # search previous names untill the same name is found
                        offset += 1
                    freq_column[i-offset] += freq_column[i]
                    duplicateIndexes.append(i)
                    male_dataFrame.drop(duplicateIndexes, axis=0,inplace=True)

            male_dataFrame.to_csv(male_outputFileName, sep=',', index=False, encoding='utf-8')

        if female_infoRead:
            female_dataSet = {'Name':female_names, 'Rank':female_ranks, 'Year':female_years, 'Freq':female_frequencies}
            female_dataFrame = pd.DataFrame(female_dataSet)

            female_dataFrame.to_csv(female_outputFileName, sep=',', index=False, encoding='utf-8')


if __name__ == "__main__":
    main ( sys.argv[1:] )
