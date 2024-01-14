#!/usr/bin/env python3

#
#   Description: 
#
#   This function plots the number of common names over time 
#
#   File Author(s): Adil Siddiqi
#   Last Date Edited: April 6 / 2023
#

import pandas as pd
import matplotlib.pyplot as plt

def commonNames(regions):
    

    validInput = False  # Sets validInput to false initially
    while not validInput:
        # Prompt user for input
        regionInput = input("Enter a valid region to evaluate or enter 0 to see valid regions: ")
        # Take the input and make it in title case example: new zealand becomes New Zealand
        regionInput = regionInput.title()
        
        # If the user wants to see the available regions then print out the list 
        if(regionInput == "0"):

            print("Available Regions: \n")
            i = 1
            for name in regions:
                print(str(i)+". "+ name)
                i+= 1
            continue
        
        # Iterate through the regions list 
        for name in regions:
            # check if the name matches the user input  
            if name == regionInput:
                # Check if there are spaces in the name important for regions with spaces like Nova Scotia
                if " " in name:

                    # This section splits the name and puts the name in camel case 
                    splitName = name.split()
                    splitName[1] = splitName[1].title()
                    splitName[0] = splitName[0].lower()
                    name = splitName[0] + splitName[1]

                    # assigns the correct input file names to the inputMale and inputFemale variables 
                    inputMale = "region/" + name + "_male.csv"
                    inputFemale = "region/" + name + "_female.csv"
                    validInput = True   # variable to exit the loop
                    break
                # Case where there are no spaces in the name like Ontario
                else:
                    # Take the name and make it lower case 
                    name = name.lower()
                    #name = name.replace(" ","")
                    # assigns the correct input file names to the inputMale and inputFemale variables
                    inputMale = "region/" + name + "_male.csv"
                    inputFemale = "region/" + name + "_female.csv"
                    validInput = True  # variable to exit the loop
                    break
        # Error handling 
        if not validInput:
            print("Invalid region name. Please try again.")

# If the loop exits, a valid input has been entered
# and the code can continue to load and analyze the data
   

  

    # Read the csv files into pandas dataframes using the inputMale and inputFemale names 
    maleDF = pd.read_csv(inputMale)
    femaleDF = pd.read_csv(inputFemale)

    # Merge the dataframe on the Name and Year columns 
    commonDF = pd.merge(maleDF, femaleDF, on = ['Name','Year'],how='inner')
    # Drop the unneccessary columns 
    commonDF = commonDF.drop(['Freq_x','Freq_y','Rank_x','Rank_y'], axis = 1)
    
    # Creates a data series that counts the values of year occurences 
    numCommon = commonDF['Year'].value_counts()
    
    #Creates a data frame with the series 
    numCommonDF = pd.DataFrame({'Year': numCommon.index, 'Frequency': numCommon.values})
    
    # Sorts the values into ascending order by year 
    numCommonDF = numCommonDF.sort_values(by='Year', ascending=True)

    # Checks if the data frame is empty if it is then print error message else make the graph
    if numCommonDF.empty:
        print("There are no common names in this region.")
    else:
        makeCommonNamesGraph(numCommonDF)
    
# Takes dataframe as parameter and creates graph
def makeCommonNamesGraph(numCommonDF):

    # Makes the Year column the x axis and the Frequency column on the y axis 
    plt.plot(numCommonDF['Year'], numCommonDF['Frequency'], color='red')
    plt.title("Frequency of Common Names between Males and Females over time")
    plt.xlabel('Year',fontsize = 14)
    plt.ylabel("Frequency",fontsize = 14)
    plt.grid(True)
    plt.show()
    plt.savefig("freqOverTime.png")
    print("The graph generated shows data from %d to %d" %(numCommonDF.loc[numCommonDF.index[0],'Year'], numCommonDF.loc[numCommonDF.index[-1],'Year']))


