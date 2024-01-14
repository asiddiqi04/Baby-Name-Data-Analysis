#!/usr/bin/env python3


# store as : name, rank, year, frequency
# name : row[3]
# rank : row[2]
# year : row[0]
# frequency : row[4]
# gender : row[1]


# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

#
#   What does this section of the code do?
#
#   This section ensures that the user entered the correct command line arguments when running the program, it then initializes
#   the variables with this information entered by the user
#
    if len(argv) < 6:
        print ( "Usage: ./california.py -i <input file name>  -f <female output file name base>  -m <male output file name base>"  )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:f:m:",["input=","femaleOutput=","maleOutput="] )
    except getopt.GetoptError:
        print ( "Usage: ./california.py -i <input file name>  -f <female output file name base>  -m <male output file name base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./california.py -i <input file name>  -f <female output file name base>  -m <male output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-f", "--femaleOutput"):
            femaleOutputFileNameBase = arg
        elif opt in ("-m", "--maleOutput"):
            maleOutputFileNameBase = arg
    femaleOutputFileName = femaleOutputFileNameBase+".csv"
    maleOutputFileName   = maleOutputFileNameBase+".csv"

#
#   What is being declared here and why?
#
#   Three lists are created, called names, numbers and ranks and the varaible total is created and initialized to 0 which will be used
#   as a counter
#
    femaleNames         = []
    femaleRanks         = []
    femaleYears         = []
    femaleFrequency     = []

    maleNames           = []
    maleRanks           = []
    maleYears           = []
    maleFrequency       = []

#   What is the overall purpose of this section of code?

#   Opens the csv file and reads its content into arrays which are to be used in the dataframe

    with open ( inputFileName ) as csvDataFile:

        # What does next do?
        # next() is a function which iterates to the next piece of data in a csv file 
        
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if ( row[1].strip() == "Female" ) :

                femaleTempName = row[3].strip()
                femaleNames.append ( femaleTempName ) 
                femaleRanks.append ( int(row[2]) )
                femaleYears.append ( int(row[0]) )
                femaleFrequency.append ( int(row[4]) )


                

            elif ( row[1].strip() == "Male" ) :
                maleTempName = row[3].strip()
                maleNames.append ( maleTempName ) 
                maleRanks.append ( int(row[2]) )
                maleYears.append ( int(row[0]) )
                maleFrequency.append ( int(row[4]) )


            femalePeople = {'Name':femaleNames,'Rank':femaleRanks, 'Year': femaleYears, 'Freq': femaleFrequency }
            femalePeople_df = pd.DataFrame(femalePeople)

            femalePeople_df = femalePeople_df.fillna(-1) 

            malePeople = {'Name': maleNames,'Rank':maleRanks, 'Year': maleYears, 'Freq': maleFrequency }
            malePeople_df = pd.DataFrame(malePeople)

            malePeople_df = malePeople_df.fillna(-1)
        

#           What is this doing?
#           The DataFrame.to_csv() function converts the Dataframe to a separate CSV file.
#           The 'utf-8' flag helps the interpreter to read the file as unicode

            femalePeople_df.to_csv(femaleOutputFileName, sep=',', index=False, encoding='utf-8')
            malePeople_df.to_csv(maleOutputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )