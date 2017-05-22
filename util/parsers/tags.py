#!/usr/local/bin/python3.6

import sys
import os
import re
import json

import Configurator

# These are the values that we are parsing on
FLAGSRGX = r"(\[VERBOSE\]|\[TRACE\]|\[DEBUG\]|\[INFO\]|\[WARN\]|\[ERROR\]|\[FATAL\])"

# This script will derive the full path to the in and out files
Inpath = ''
Outpath = ''


def Main(infile):
    outfile = f"{infile}.out"

    print (f"Proceeding with filename {infile} as input.")
    print (f"Proceeding with filename {outfile} as output.")
    
    configDict = Configurator.SetConfigurations(['input', 'output'])

    Inpath = configDict['input']
    Outpath = configDict['output']

    print (f'Using input directory: {Inpath}')
    print (f'Using output directory: {Outpath}')

    if len(Inpath)<=0 or len(Outpath)<=0:
        print (f'Inpath or Outpath could not be determined. Please ensure this script is being ran from inside the project directory structure. This process will now terminate.')
        return

    inFileNamePath = Inpath + infile
    outFileNamePath = Outpath + outfile

    print (f'Using input full filename path: {inFileNamePath}')
    print (f'Using output full filename path: {outFileNamePath}')

    ParseMap(inFileNamePath, outFileNamePath)


def ParseMap(infile, outfile):
    expr = re.compile(FLAGSRGX)

    # Because the first letter of each tag is unique we slice this letter from 
    #   the matching string and write just this letter to the outfile. 
    with open(infile, 'r') as instream:
        with open(outfile, 'w') as outstream:
            for line in instream:
                word = expr.search(line)
                if (word):
                    outstream.write(word.group()[1])

    print ("--DoneonRings--") 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("A file name is required as argument i.e.$tagPrs.py myinputfile.txt")
        print ("This process will now close.")
    else:
        Main(sys.argv[1])

#TODO: if no input file name is given display the files in the Input/ to the user
