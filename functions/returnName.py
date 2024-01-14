#!/usr/bin/env python3

#
#   Description: This is a helper function used to return a name with proper capitalization, along with that there is some test cases
#                and a way to test the funciton below

import os

def returnName(name):

    name = name.title()

    #Keep this for loop if we want anythin after ' to be lowercase, otherwise we can delete
    for i in range(len(name)):
        if name[i] == '\'' and i != len(name) - 1:
            tempName = list(name)
            tempName[i+1] = tempName[i+1].lower()
            name = "".join(tempName)

    # Note: this function prints the name without a newline at the end
    return name