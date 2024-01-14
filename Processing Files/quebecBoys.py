#!/usr/bin/env python3


# store as : name, rank, year, frequency


# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
import glob
from itertools import accumulate
import numpy as np
from operator import itemgetter
 
def main(argv):

    #
    #   What does this section of the code do?
    #
    #   This section ensures that the user entered the correct command line arguments when running the program, it then initializes
    #   the variables with this information entered by the user
    #

    if len(argv) < 4:
        print("Usage: ./quebecBoys.py -i <input file name> -o <output file name base>")
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt(argv, "i:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("Usage: ./quebecBoys.py -i <input file name> -o <output file name base>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ./quebecBoys.py -i <input file name> -o <output file name base>")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + ".csv"

    #
    #   What is being declared here and why?
    #
    #   Three lists are created, called names, numbers and ranks and the variable total is created and initialized to 0 which will be used
    #   as a counter
    #
    names = []
    ranks = []
    years = []
    frequency = []

    #   What is the overall purpose of this section of code?

    #   Opens the csv file and reads its content into arrays which are to be used in the dataframe

    with open(inputFileName) as csvDataFile:

        # What does next do?
        # next() is a function which iterates to the next piece of data in a csv file

        next(csvDataFile)

        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            for i in range(1, 43):
                if (int(row[i])) != 0:
                    tempName = row[0].strip()
                    names.append(tempName)
                    frequency.append(int(row[i]))
                    years.append(int(1979 + i))

        people = {'Name': names, 'Year': years, 'Freq': frequency}

        # Remove duplicates

        people_df = pd.DataFrame(people)

        # Fix duplicate test by dropping duplicates based on 'Name' column

        people_df.drop_duplicates(subset='Name', keep='first', inplace=True)

        # Fix ranks order test by converting ranks to integers

        people_df['Rank'] = people_df.groupby(['Year'])['Freq'].rank(ascending=False, method='min').astype(int)

        people_df.sort_values(by=['Year', 'Rank'], inplace=True)

        # Reorder columns

        Pcolumns_titles = ["Name", "Rank", "Year", "Freq"]
        people_df = people_df.reindex(columns=Pcolumns_titles)

        # Convert names to uppercase

        people_df['Name'] = people_df['Name'].str.upper()

        # Output to CSV file

        people_df.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')


if __name__ == "__main__":
    main(sys.argv[1:] )


