
How To Set Up Program:

Raw data files are provided in Folder: Raw_Data
All files were obtained from links on courselink
For each file, if there is a header or anything above the csv data then delete those rows

Processing Each File:

Alberta:
Usage: ./albertaProcessing -i <fileName>
*Some names had a ‘ in front of the names that were manually deleted*

Ireland:
Usage: ./irelandProcessing -m <maleFileName> -f <femaleFileName>
**Note The last half of the ireland file was deleted as it was the ranking system which did not align with our intended ranking system**

California:
Usage: ./california.py -i <input file name>  -f <female output file name base>  -m <male output file name base>

Quebec:
Male file:
Usage: ./quebecBoys.py -i <input file name> -o <output file name base>

Female file:
Usage: ./quebecGirls.py -i <input file name> -o <output file name base>

Ontario:
Usage: ./ontarioScript.py -m <maleFileName> -f <femaleFileName>
*Duplicate manually deleted 

Nova Scotia:
Usage: ./novaScotiaScript.py -i <inputFileName> 
*Duplicate manually deleted

Australia:
Usage: ./australiaScript.py -i <inputFileName>

New Brunswick:
Usage: ./NBRead.py -i <inputFileName>

New Zealand:
Usage: ./NZRead.py -i <inputFileName>




All processed files must be in folder: region
All question functions must be in folder: functions
All raw files must be in folder: Raw Files
All processing files must be in folder: Processing Files

Then the program is run as ./main.py


Testing File Information

Column Length Test :  This tests to make sure that all of the columns are the same length
Name Existing Test: This tests to make sure all rows contain a name
Frequency Test : This tests to make sure that there are no frequencies of 0
Name Alpha Test : This tests to make sure the first char of each name is an alpha character
Extraneous Space Test : This test to make sure there are no extraneous spaces around names
Duplicate Test : This test to make sure there are no duplicate names in the same year
Tied Rank Test : This tests that if 2 entries have the same rank then they must also have the same freq
Freq/Ranks Test : This tests that if 2 entries have the same frequency, then they have the same rank
Ranks Order Test : This tests that the ranking system was done correctly, Ex. (1, 1, 3, 4)
