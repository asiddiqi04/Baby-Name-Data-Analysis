#!/usr/bin/env python3
#
#   Description: 
#
#   This function returns the location names of all the files, except for the
#   namsor california file
#
#   File Author(s): Ben Holbrook
#   Last Date Edited: April 6th / 2023
#

import os

def getLocNames():

    fileNameList = []
    locList = []

    # using os.scandir we scan the region folder for all of the filenames contained in the folder
    with os.scandir('region/') as entries:
        for entry in entries:
            fileNameList.append(entry.name)

    # for all of the filenames in the list
    for fileName in fileNameList:
        # Don't use the namesor file (it is only used for the ethinic regions requirement)
        if fileName != "namsor_name-origin_california_male_last19y.csv":
            counter = 0
            locationFound = 0
            # get the index before the first _
            while fileName[counter] != '_':
                counter += 1
            # if the location is already in the list then dont add
            for locations in locList:
                if locations == fileName[:counter]:
                    locationFound += 1
            # if the location is not yet in the list then append it up until the first _ which will just be the location name
            if locationFound == 0:
                locList.append(fileName[:counter])

    # reuturn the list of all valid location names
    return locList
