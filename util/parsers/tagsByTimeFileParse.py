#!/usr/local/bin/python3.6

import sys
import os
import re

import configurator

'''
Parse structured log files by their tags. 
Return structured output; rows are ten-minute segments of a day; 
columns are the counts of each tag type.
Standalone - Reads cl-argument as input file name.
'''


def Main(infile):
    configDict = configurator.SetConfigurations(['input', 'temp'])
    inFileNamePath = configDict['input'] + infile
    outFileNamePath = configDict['temp'] + ig.Setup(infile)

    tSegments, targetDay = ParseMap(inFileNamePath)

    with open(outFileNamePath, 'w') as outstream:
        for i in tSegments:
            outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in tSegments[i]]) + '\n'
            outstream.write(outst) 

    print ("--DoneonRings--") 


def ParseMap(infile):
    motifRgx = r'^\[[0-9]{4}\-.+?].+?]'

    # Dictionary for 10 minute segments of a given day
    tSegments = dict.fromkeys([i for i in range(144)])

    # Initialize the dictionary. The range is the number of tags we expect. 
    for i in range(len(tSegments)):
        tSegments[i] = [0 for i in range(6)]

    motifRgxC = re.compile(motifRgx)
    lastTime = ''
    
    with open(infile, 'r') as instream:
        for line in instream:
            motif = motifRgxC.search(line)

            if (motif):
                # Regex for the prefix-structure of each row.
                motifsplit = re.split('\[|\]|\-|T|:|\.', motif.group())

                year = motifsplit[1]
                month = motifsplit[2]
                day = motifsplit[3]
                hour = motifsplit[4]
                minute = motifsplit[5]
                second = motifsplit[6]
                sev = motifsplit[11]

                if len(lastTime) <= 0:
                    lastTime = (year + month + day)
                
                # If the log changes days, we stop parsing.
                if lastTime != (year + month + day):
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
