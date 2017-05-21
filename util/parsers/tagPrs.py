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

    print (Inpath)
    print (Outpath)

    return
    expr = re.compile(FLAGSRGX)
    somestring = r"alphabet[TRACE]soup"

    with open(inpath, 'r') as instream:
        with open(outpath, 'w') as outstream:
            for line in instream:
                word = expr.search(line)
                if (word):
                    outstream.write(word.group() + '\n')

    print ("--DoneonRings--") 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("A file name is required as argument i.e.$tagPrs.py myinputfile.txt")
        print ("This process will now close.")
    else:
        Main(sys.argv[1])
