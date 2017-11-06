import sys
import re

from os import listdir
from os.path import isfile, join



'''
 Takes a target directory and reads any/all files that are contained inside.
 Target files are assumed to be log files where each record is separated by a newline.
 Returns a LIST where each line is another record from the log files.
 The first record of the first file read will dictate the starting timestamp to begin reading the files.
 This reader will read records only from the starting timestamp until midnight or end of 
 end of files, whichever comes first. This does include records contained in a file that 
 contains record for the next day. 
'''
def ReadAllFilesInDirectory(targetDirPath):
    filedata = []

    # Use OS library methods to collect list of all files in target dir
    # List generated contains full path of all input files in target directory
    inputFileList = [join(targetDirPath,f) for f in listdir(targetDirPath) if isfile(join(targetDirPath, f))]

    # ASSUMPTION
    # Input files are named with a unique suffix that can be sorted in ascending order 
    # similar to a timestamp
    # e.g. infile.2017_12_30.log, logfile.2017123023595900.log, log11111.log, log11112.log, log11119.log
    inputFileList.sort()

    # TODO move regex to a static file to allow picking and choosing of consistant patterns.
    firstRecordTimestamp = ''
    timestampPrefixRegex = re.compile(r'^\[[0-9]{4}\-.+?].+?]')

    for infile in inputFileList:
        temp_tSegments, timestamp = ParseMap(infile)

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

    return filedata 



'''
 Takes 
    infile := full path input file
    startedTimestamp := timestamp marker when we started reading files from directory
    prefixRe := timestamp prefix regex pattern
 Reads lines from file until end of file or record timestamp is found to be a different day.
'''
def ParseMap(infile, startedTimestamp, prefixRe):    
    with open(infile, 'r') as instream:
        for line in instream:
            motif = prefixRe.search(line)

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
    # target a default directory
    targetDirPath = '/home/bryan/GitRepos/LogMining/data/input'

    ReadAllFilesInDirectory(targetDirPath)
