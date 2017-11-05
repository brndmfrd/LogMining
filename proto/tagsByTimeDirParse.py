#!/usr/local/bin/python3.6

# Design:
# Given a directory name will read the files in the directory.
# The files are parsed for the target data and the resultant data is aggregted.

# NOTES:
# It will be best to have a naming convention for the files such that the names can be sorted ascending and 
# correlate to their respective timestamps. (e.g. log001 - 3:15pm; log002 - 3:16pm;)
import sys
import re

from os import listdir
from os.path import isfile, join

import configurator
import tagsByTimeFileParse


def Main():
    # ================ Establish input and output directories ===============================
    outfile = 'tagsByTime.out'
    print (f"Proceeding with filename {outfile} as output.")

    # These string values must match the keyss in the config file
    targetSource = 'input'
    targetDestination = 'output'

    configDict = configurator.SetConfigurations([targetSource, targetDestination])

    inpath = configDict[targetSource]
    outpath = configDict[targetDestination]

    print (f'Using input directory: {inpath}')
    print (f'Using output directory: {outpath}')

    if len(inpath)<=0 or len(outpath)<=0:
        print (f'inpath or outpath could not be determined. Please ensure this script is being ran from inside the project directory structure. This process will now terminate.')
        return

    inFileNamePath = inpath
    outFileNamePath = outpath + outfile

    print (f'Using input full filename path: {inFileNamePath}')
    print (f'Using output full filename path: {outFileNamePath}')
    
    # =============== Generate list of files contained by input directory ==================
    inputFileList = [f for f in listdir(inFileNamePath) if isfile(join(inFileNamePath, f))]
    inputFileList.sort()
    print (f'There are \'{len(inputFileList)}\' input files that will be parsed.')

    # =============== Call parser for each input file ======================================
    # TODO get dictionary from fileparser
    # Dictionary for 10 minute segments of a given day
    tSegments = dict.fromkeys([i for i in range(144)])

    # Initialize the dictionary. 
    # TODO: set the range below to the number of configured tags.
    for i in range(len(tSegments)):
        tSegments[i] = [0 for i in range(6)]

    timestamp = ''
    lastTimestamp = ''
    recordCount = 0

    # Add the returned values to our local master list
    for infile in inputFileList:
        print (f'Begin parsing file \'{infile}\'')
        temp_tSegments, timestamp = tagsByTimeFileParse.ParseMap(inFileNamePath + infile)

        if len(lastTimestamp)<=0:
            lastTimestamp = timestamp
            print (f'Initial timestamp: {timestamp}')

        if timestamp != lastTimestamp:
            print (f'Timestamp changed to: {timestamp}')
            break

        for row in range(0, len(temp_tSegments)):
            for i in range(0, len(temp_tSegments[row])):
                tSegments[row][i] = tSegments[row][i] + temp_tSegments[row][i]
        recordCount += 1

    print (f'Processed \'{recordCount}\' files.')

    # Write the output
    # Todo find a more robust way of doing this with csv
    with open(outFileNamePath, 'w') as outstream:
        for i in tSegments:
            outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in tSegments[i]]) + '\n'
            outstream.write(outst) 


'''
If this script is started we give the option to add 'yes' as an argument to skip the prompt at the start.
$python tagsByTimeDirParse.py 
or
$python tagsByTimeDirParse.py yes
'''
if __name__ == "__main__":
    continueFlag = 'do not continue'

    if len(sys.argv) == 2:
        continueFlag = sys.argv[1]
    else:
        print ('This file will begin the process of parsing all files contained inside of the input directory.')
        print ('Depending on the size and quanity of the files in the input directory, this process may take a long while.')
        
        continueFlag = input('Would you like to proceed? [yes/Any]')

    if continueFlag == 'yes':
        Main()
    else:
        print (f'User input \'{continueFlag}\' does not match \'yes\'')
        print ('This script will now terminate. Toodle loo.')
