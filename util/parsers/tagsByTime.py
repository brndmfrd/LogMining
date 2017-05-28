#!/usr/local/bin/python3.6

import sys
import os
import re
#import json
#import csv

#import Configurator
import DefaultConfig

# When running this script standalone we use a default configuration
# We expect the default config to give us an out path to temp/
def Main(infile):
    # Use out default in/out paths
    inFileNamePath, outFileNamePath = DefaultConfig.Setup(infile)

    # Perform the parsing
    tSegments = ParseMap(inFileNamePath)

    print ('Finished parsing.')
    print ('Begin writing to output file.')

    # Write the output
    # Todo find a more robust way of doing this with csv
    with open(outFileNamePath, 'w') as outstream:
        for i in tSegments:
            outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in tSegments[i]]) + '\n'
            outstream.write(outst) 

    print ("--DoneonRings--") 


# Parses a given input file for timestamp and log level tag
# Returns a structured data representing the count of the tags per 10 minute increments for one day.
# If the day (timestamp) changes while reading the file, the parsing does not continue parsing records for a  different day.
# In: Full filename path of input file; this file will be read.
# Out: Dictionary and datetime
def ParseMap(infile):
    # TODO: get the regex value that are project specific from a config file.

    # We must begin with a simple assumption:
    #   Every new valid log record begins with the same two tags [timestamp][flag]
    # Example target from log file: [2015-09-20T19:59:24.5499068-04:00] [DEBUG]

    motifRgx = r'^\[[0-9]{4}\-.+?].+?]'

    # Dictionary for 10 minute segments of a given day
    tSegments = dict.fromkeys([i for i in range(144)])

    # Initialize the dictionary. 
    # TODO: set the range below to the number of configured tags.
    for i in range(len(tSegments)):
        tSegments[i] = [0 for i in range(6)]

    motifRgxC = re.compile(motifRgx)
    lastTime = ''
    
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

               # TODO use switch stmnt 
                # Count DEBUG - uses first letter of tag
                if sev[0] == 'D':
                    tSegments[mapTimeseg][0] += 1 
                # Count VERBOSE - uses first letter of tag
                if sev[0] == 'V':
                    tSegments[mapTimeseg][1] += 1 
                # Count INFO - uses first letter of tag
                if sev[0] == 'I':
                    tSegments[mapTimeseg][2] += 1 
                # Count WARN - uses first letter of tag
                if sev[0] == 'W':
                    tSegments[mapTimeseg][3] += 1 
                # Count ERROR - uses first letter of tag
                if sev[0] == 'E':
                    tSegments[mapTimeseg][4] += 1 
                # Count FATAL - uses first letter of tag
                if sev[0] == 'F':
                    tSegments[mapTimeseg][5] += 1 

        return tSegments, lastTime


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("A file name is required as argument i.e.$tagPrs.py myinputfile.txt")
        print ("This process will now close.")
    else:
        Main(sys.argv[1])

#TODO: if no input file name is given display the files in the Input/ to the user
