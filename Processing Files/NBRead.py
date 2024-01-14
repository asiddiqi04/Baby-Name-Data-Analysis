#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd
from itertools import accumulate
import numpy as np
from operator import itemgetter

def main (argv):

#
#   What does this section of the code do?
#   If the command line argument is less than 6 than it prints out the message in the conditional
#   
    if len(argv) < 2:
        print ( "Usage: ./NBRead.py -i <input file name>" )
	#exits the program
        sys.exit(2)
    try:
	#Try and except used for error handling
        (opts, args) = getopt.getopt ( argv,"i:",["input ="] )
    except getopt.GetoptError:
        print ( "Usage: ./NBRead.py -i <input file name>" )
        sys.exit(2)
# Basically what this loop is doing is checking what the command line argument is and depending on what it is it will create a different output file name 
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./NBRead.py -i " )
            sys.exit()

        elif opt in ( "-i", "--input"):
            inputFileName = arg
    #Reading Csv File
    df = pd.read_csv(inputFileName) # loading the file as a dataframe
    #Column Names
    df.columns = ['Year','Sex','Name','Frequency']
    #Initializing Lists
    MNames = []
    MFreq = []
    MYear = []
    MNameFreqYear = []
    FNames = []
    FFreq = []
    FYear = []
    FNameFreqYear = []
    #Splitting Dataframes
    female_df = df[df['Sex'] == 'F']
    male_df = df[df['Sex'] == 'M']
    
    df.columns =['Year','Sex','Name','Frequency']
    
    female_df = df[df['Sex'] == 'F']
    male_df = df[df['Sex'] == 'M']

    male_df = male_df.reset_index() 
    male_df.sort_values(by=['Year','Frequency'], ascending = [True,False], inplace = True)
    Mlist = male_df.values.tolist()

    for i in range (0,len(Mlist)):
        Mlist[i].pop(0)
        Mlist[i].extend('1')
    Mdf = pd.DataFrame(Mlist)
    Mdf.columns = ['Year','Sex','Name','Freq','Rank']
    Mdf = Mdf.drop('Sex', axis=1)
    #print(df)
    
    Mdf['Rank'] = Mdf.groupby(['Year'])['Freq'].rank(ascending=False)
    Mcol = ['Rank']
    Mdf[Mcol] = Mdf[Mcol].applymap(np.int64)

    Mcolumns_titles = ["Name","Rank","Year","Freq"]
    Mdf=Mdf.reindex(columns=Mcolumns_titles)

    Mdf.to_csv('newBrunswick_male.csv', index=False)

    #Female Name

    female_df = female_df.reset_index() 
    female_df.sort_values(by=['Year','Frequency'], ascending = [True,False], inplace = True)
    list = female_df.values.tolist()

    for i in range (0,len(list)):
        list[i].pop(0)
        list[i].extend('1')
    Fdf = pd.DataFrame(list)
    Fdf.columns = ['Year','Sex','Name','Freq','Rank']
    Fdf = Fdf.drop('Sex', axis=1)
    #print(df)
    
    Fdf['Rank'] = Fdf.groupby(['Year'])['Freq'].rank(ascending=False)
    Fcol = ['Rank']
    Fdf[Fcol] = Fdf[Fcol].applymap(np.int64)

    Fcolumns_titles = ["Name","Rank","Year","Freq"]
    Fdf=Fdf.reindex(columns=Fcolumns_titles)

    Fdf['Name'] = Fdf['Name'].str.upper()
    Fdf['Rank'] = Fdf.groupby(['Year'])['Freq'].rank(ascending=False,method='min')
    Fcol = ['Rank']
    Fdf[Fcol] = Fdf[Fcol].applymap(np.int64)

    Fcolumns_titles = ["Name","Rank","Year","Freq"]
    Fdf=Fdf.reindex(columns=Fcolumns_titles)
    Fdf['Name'] = Fdf['Name'].str.upper()
    Fdf.to_csv('newBrunswick_female.csv', index=False)

    

if __name__ == "__main__":
    main (sys.argv[1:] )