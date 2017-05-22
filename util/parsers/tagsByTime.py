#!/usr/local/bin/python3.6

import sys
import os
import re
import json

import Configurator

# These are the values that we are parsing on
FLAGSRGX = r"(\[VERBOSE\]|\[TRACE\]|\[DEBUG\]|\[INFO\]|\[WARN\]|\[ERROR\]|\[FATAL\])"

# [2015-09-20T19:59:24.5499068-04:00] [DEBUG]
# This assumes lines that start with a bracket start with a timestamp bracket.
TIMESTAMPRGX = r'(^\[.+?\.)'
#DATERGX = r'([0-9]{4}\-[0-9]{2}\-[0-9]+)'
#TIMERGX = r'[0-9]+\:[0-9]{2}\:[0-9]{2})'

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
    timestampRgxC = re.compile(TIMESTAMPRGX)
    #dateRgxC = re.compile(DATERGX)
    #timeRgxC = re.compile(TIMERGX)
    flagRgxC = re.compile(FLAGSRGX)
    timeSegments = []
    modulus = 0
    previousDate = ''

    with open(infile, 'r') as instream:
        for line in instream:
            time = timestampRgxC.search(line)
            flag = flagRgxC.search(line)
            
            if (time and flag):
                datetime = time.group().split('T')
                date = datetime[0]
                time = datetime[1]
                
                print ('Date: ' + date)
                print ('Time: ' + time)

                if(len(previousDate)<=0):
                    previousTime = time
                
                if(previousTime is not time):
                    print ('The log has rolled over to the next day. Parser will now self terminate. Hasta la vista.')
                    return
                
                #outstream.write(word.group()[1])

    print ("--DoneonRings--") 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("A file name is required as argument i.e.$tagPrs.py myinputfile.txt")
        print ("This process will now close.")
    else:
        Main(sys.argv[1])

#TODO: if no input file name is given display the files in the Input/ to the user
