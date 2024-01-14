#!/usr/bin/env python3
#   File Author(s): Adil Siddiqi
#   Last Date Edited: March 11 / 2023

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def main (argv):
        
    if len(argv) < 2:
        print ( "Usage: ./novaScotiaScript.py -i <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:",["input="])
        print("opts:", opts)
        print("args:", args)
    except getopt.GetoptError:
        print ( "Usage: ./novaScotiaScript.py -i <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./novaScotiaScript.py -i <input file name>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        
    
    




    namesMale = []
    rankMale = []
    yearMale = []
    freqMale = []


    namesFemale = []
    rankFemale = []
    yearFemale = []
    freqFemale = []

    

   

    with open(inputFileName) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)  # skip the header row
        
        for row in csvReader:
            year = int(row[0])
            gender = row[1]
            name = row[2]
            freq = int(row[3])
            
            if gender == "M":
                yearMale.append(year)
                namesMale.append(name)
                freqMale.append(freq)
                rankMale.append(0)
                
                

            elif gender == "F":
                yearFemale.append(year)
                namesFemale.append(name)
                freqFemale.append(freq)
                rankFemale.append(0)
     
    
    rMale = 0
    prevYear = yearMale[0]
    for i in range(len(rankMale)):
        currYear = yearMale[i]
        #repeat = i
        if currYear == prevYear:
            rMale = rMale + 1
            rankMale[i]= rMale
        elif currYear != prevYear:
            prevYear += 1
            rMale = 1
            rankMale[i] = rMale


    rFemale = 0
    prevYear = yearFemale[0]
    
    for i in range(len(rankFemale)):
        currYear = yearFemale[i]
        if currYear == prevYear:
            rFemale = rFemale + 1
            rankFemale[i]= rFemale
        elif currYear != prevYear:
            prevYear += 1
            rFemale = 1
            rankFemale[i] = rFemale
    
   

    print(len(yearMale))
    print(len(rankMale))



    maleDF = pd.DataFrame({'Name':namesMale, 'Rank':rankMale, 'Year':yearMale, 'Freq':freqMale})
    femaleDF = pd.DataFrame({'Name':namesFemale, 'Rank':rankFemale, 'Year':yearFemale, 'Freq':freqFemale})


    maleDF['Rank'] = maleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')
    femaleDF['Rank'] = femaleDF.groupby(['Year'])['Freq'].rank(ascending = False, method ='min')


    maleDF['Name'] = maleDF['Name'].str.upper()
    femaleDF['Name'] = femaleDF['Name'].str.upper()

    

    maleDF['Rank'] = maleDF['Rank'].astype(int)
    femaleDF['Rank'] = femaleDF['Rank'].astype(int)
    

    maleDF.to_csv('novaScotia_male.csv', index=False)
    femaleDF.to_csv('novaScotia_female.csv', index=False)

    print(maleDF)
    print(femaleDF)

if __name__ == "__main__":
    main ( sys.argv[1:] )