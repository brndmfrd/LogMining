#!/usr/local/bin/python3.6

import sys
import os
import re
import json
import csv

import Configurator

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
    # TODO: get the regex value that are project specific from a config file.

    # We must begin with a simple assumption:
    #   Every new valid log record begins with the same two tags [timestamp][flag]
    # Example target from log file: [2015-09-20T19:59:24.5499068-04:00] [DEBUG]

    motifRgx = r'^\[[0-9]{4}\-.+?].+?]'

    # Dictionary for 10 minute segments of a given day
    tSegments = dict.fromkeys([i for i in range(144)])
    for i in range(len(tSegments)):
        tSegments[i] = 0

    motifRgxC = re.compile(motifRgx)
    lastTime = ''
    lastMinute = ''
    
    with open(infile, 'r') as instream:
        for line in instream:
            motif = motifRgxC.search(line)

            if (motif):
                # Attempt an easy split. This should work most/all of the time, based on our assumptions.
                motifsplit = re.split('\[|\]|\-|T|:|\.', motif.group())

                year = motifsplit[1]
                month = motifsplit[2]
                day = motifsplit[3]
                hour = motifsplit[4]
                minute = motifsplit[5]
                second = motifsplit[6]
                sev = motifsplit[11]

                # This is where we check our assuptions and validate the data we just collected.
                # If the data we collected does not match our assumptions (e.g. 'year' is empty)
                # TODO

                if len(lastTime) <= 0:
                    lastTime = (year + month + day)
                
                if lastTime != (year + month + day):
                    print ('The log has rolled over to another day. No further parsing will be done. Processing will complete with data collected until this point.')
                    break
                
                # map hours to 10 minute segments
                mapHour = (int(hour) * 6)
                mapMinute = int(int(minute) / 10)
                mapTimeseg = (mapHour + mapMinute)

                # Just count DEBUG - uses first letter of tag
                if sev[0] == 'D':
                    #print(str(mapTimeseg) + ' ' + str(tSegments[mapTimeseg]))
                    tSegments[mapTimeseg] += 1 

        # TODO find a more robust way of doing this with csv
        with open(outfile, 'w') as outstream:
            for i in tSegments:
                outstream.write(str(i) + ' ' + str(tSegments[i]) + '\n')

    print ("--DoneonRings--") 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("A file name is required as argument i.e.$tagPrs.py myinputfile.txt")
        print ("This process will now close.")
    else:
        Main(sys.argv[1])

#TODO: if no input file name is given display the files in the Input/ to the user