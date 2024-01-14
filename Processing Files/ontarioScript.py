#!/usr/bin/env python3
#   File Author(s): Adil Siddiqi
#   Last Date Edited: March 11 / 2023
#

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def main ( argv ):
    
    if len(argv) < 2:
        print ( "Usage: ./ontarioScript.py -m <male file name> -f <female file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"m:f:",["input="] )
        print("opts:", opts)
        print("args:", args)

    except getopt.GetoptError:
        print ( "Usage: ./ontarioScript.py -m <male file name> -f <female file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./ontarioScript.py -m <male file name> -f <female file name>" )
            sys.exit()
        elif opt in ( "-m", "--male_csv"):
            inputMale = arg
        elif opt in ("-f", "--female_csv"):
            inputFemale = arg
        else:
            print("error")
            sys.exit(2)
        

    maleDF = pd.read_csv(inputMale)
    femaleDF = pd.read_csv(inputFemale)

    maleDF = maleDF.reindex(columns = ['Name','Rank','Year','Freq'])
    femaleDF = femaleDF.reindex(columns = ['Name','Rank','Year','Freq'])

    maleDF['Name'] = maleDF['Name'].str.upper()
    femaleDF['Name'] = femaleDF['Name'].str.upper()


    maleDF['Rank'] = maleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')
    femaleDF['Rank'] = femaleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')

    maleDF['Rank'] = maleDF['Rank'].astype(int)
    femaleDF['Rank'] = femaleDF['Rank'].astype(int)



    maleDF.to_csv('ontario_male.csv', index=False)
    femaleDF.to_csv('ontario_female.csv', index=False)



    print(maleDF)
    print(femaleDF)

if __name__ == "__main__":
    main ( sys.argv[1:] )