#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd
import glob
from itertools import accumulate
import numpy as np
from operator import itemgetter

def main (argv):

#
#   What does this section of the code do?
#   If the command line argument is less than 6 than it prints out the message in the conditional
#   
    if len(argv) < 2:
        print ( "Usage: ./NZRead.py -i <input file name>" )
	#exits the program
        sys.exit(2)
    try:
	#Try and except used for error handlings
        (opts, args) = getopt.getopt ( argv,"i:",["input ="] )
    except getopt.GetoptError:
        print ( "Usage: ./NZRead.py -i <input file name>" )
        sys.exit(2)
# Basically what this loop is doing is checking what the command line argument is and depending on what it is it will create a different output file name 
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./NZRead.py -i" )
            sys.exit()

        elif opt in ( "-i", "--input"):
            inputFileName = arg
    #Reading Csv File
    df = pd.read_csv(inputFileName) # loading the file as a dataframe

    df.columns =['Year','Sex','Name','Frequency']
    male_df = df[df['Sex'] == 'M']
    female_df = df[df['Sex'] == 'F']
    
    female_df = female_df.reset_index() 
    female_df.sort_values(by=['Year','Frequency'], ascending = [True,False], inplace = True)
    list = female_df.values.tolist()

    for i in range (0,len(list)):
        list[i].pop(0)
        list[i].extend('1')
    Fdf = pd.DataFrame(list)
    Fdf.columns = ['Year','Sex','Name','Freq','Rank']
    Fdf = Fdf.drop('Sex', axis=1)

    Fdf['Rank'] = Fdf.groupby(['Year'])['Freq'].rank(ascending=False,method='min')
    Fcol = ['Rank']
    Fdf[Fcol] = Fdf[Fcol].applymap(np.int64)

    Fcolumns_titles = ["Name","Rank","Year","Freq"]
    Fdf=Fdf.reindex(columns=Fcolumns_titles)
    Fdf['Name'] = Fdf['Name'].str.upper()
    for year in range (1900,2022):
        name = []
        for i in range (0,len(Fdf)):
            if (Fdf.loc[i,'Year'] == year):
                #print(Fdf.loc[i,'Name'],i)
                name.append(Fdf.loc[i,'Name'])

        count_dict = {}
        for val in name:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1

        # print the values that appear more than once
        for val, count in count_dict.items():
            if count > 1:
                print(val)



    Fdf.to_csv('newZealand_female.csv', index=False)

#Male Name

    #print(male_df)

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
    
    Mdf['Rank'] = Mdf.groupby(['Year'])['Freq'].rank(ascending=False, method='min')
    Mcol = ['Rank']
    Mdf[Mcol] = Mdf[Mcol].applymap(np.int64)
    Mcolumns_titles = ["Name","Rank","Year","Freq"]
    Mdf=Mdf.reindex(columns=Mcolumns_titles)
    Mdf['Name'] = Mdf['Name'].str.upper()
    Mdf.to_csv('newZealand_male.csv', index=False)



    
if __name__ == "__main__":
    main (sys.argv[1:] )
