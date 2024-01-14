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
        print ( "Usage: ./australiaScript.py -i <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:",["input="])
        print("opts:", opts)
        print("args:", args)
    except getopt.GetoptError:
        print ( "Usage: ./autraliaScript.py -i <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./australiaScript.py -i <input file name>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg



    australiaDF = pd.read_csv(inputFileName)
    
    maleDF = australiaDF[australiaDF["Gender"] == "Male"]
    femaleDF = australiaDF[australiaDF["Gender"] == "Female"]

    maleDF = maleDF.drop(["Gender"], axis = 1)
    femaleDF = femaleDF.drop(["Gender"], axis = 1)

    maleDF = maleDF.reindex(columns = ["Name", "Rank", "Year","Count"])
    femaleDF = femaleDF.reindex(columns = ["Name", "Rank", "Year","Count"])

    maleDF = maleDF.rename(columns = {"Count" : "Freq"})
    femaleDF = femaleDF.rename(columns = {"Count" : "Freq"})

    maleDF['Name'] = maleDF['Name'].str.upper()
    femaleDF['Name'] = femaleDF['Name'].str.upper()


    maleDF['Rank'] = maleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')
    femaleDF['Rank'] = femaleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')

    maleDF['Rank'] = maleDF['Rank'].astype(int)
    femaleDF['Rank'] = femaleDF['Rank'].astype(int)

    sortedMale = maleDF.sort_values(['Year', 'Rank'], ascending=[True, True])
    sortedFemale = femaleDF.sort_values(['Year', 'Rank'], ascending=[True, True])

    sortedMale.to_csv('australia_male.csv', index=False)
    sortedFemale.to_csv('australia_female.csv', index=False)


    print(sortedMale)
    print(sortedFemale)
    


if __name__ == "__main__":
    main ( sys.argv[1:] )

