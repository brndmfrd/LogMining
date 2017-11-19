import sys
import re

from os import listdir
from os.path import isfile, join


firstRecordTimestamp = ''


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
    #timestampPrefixRegex = re.compile(r'^\[[0-9]{4}\-.+?].+?]')
    timestampPrefixRegex = re.compile(r'^\[[0-9]{4}\-[0-9]{2}\-[0-9]{2}')

    for infile in inputFileList:
        print(f'file: {infile}')
        goodReads, badRecordCount, lastRecordTimestamp = ReadFromFile(infile, timestampPrefixRegex)

        filedata.extend(goodReads)
        
        print(badRecordCount)

        if lastRecordTimestamp != firstRecordTimestamp:
            if len(firstRecordTimestamp)<=0:
                # This means we read at least one file and did not find a timestamp in it.
                # Warning?
                print('How did you manage to read a file with no suitable timestamp?')
            else:
                print('We stopped matching')
                break
        
    return filedata



'''
 Takes 
    infile := full path input file
    lastTime := timestamp marker when we started reading files from directory
    prefixRe := timestamp prefix regex pattern
 Processes
    Reads lines from file until end of file or record timestamp is found to be a different day.
 Returns
    goodRecords := list of all records that match the target date
    badRecordCount := lines read from the file that do not match proper log file format
    recordDate := date from last read record (this includes non-matching date)
'''
def ReadFromFile(infile, prefixRe):     
    goodRecords = []
    recordDate = ''
    badRecordCount = 0
    global firstRecordTimestamp

    with open(infile, 'r') as instream:
        for line in instream:
            motif = prefixRe.search(line)

            if (motif):
                # Regex for the prefix-structure of each row.
                motifsplit = re.split('\[|\]|\-|T|:|\.', motif.group())

                year = motifsplit[1]
                month = motifsplit[2]
                day = motifsplit[3]

                #hour = motifsplit[4]
                #minute = motifsplit[5]
                #second = motifsplit[6]
                #sev = motifsplit[11]

                # Append these values together to make a date (19991230)
                recordDate = (year + month + day)

                # Either first timestamp or record read is from a different day
                if firstRecordTimestamp != recordDate:
                    if len(firstRecordTimestamp) <= 0:
                        # set script-wide scope variable - one script one firstRecordTimestamp
                        firstRecordTimestamp = recordDate
                        print(f'setting the firstRecordTimestamp:{firstRecordTimestamp}')
                    else: 
                        print('We stopped matching inside of this file')
                        break
                
                goodRecords.append(line)
            else:
                badRecordCount = badRecordCount + 1


    print(f'count good reads {len(goodRecords)}')
    print(f'count bad reads {badRecordCount}')    
    print(f'target record date {firstRecordTimestamp}')
    print(f'last record date {recordDate}')
    return goodRecords, badRecordCount, recordDate



if __name__ == "__main__":
    # target a default directory
    targetDirPath = '/home/bryan/GitRepos/LogMining/data/temp'
    #targetDirPath = '/home/bryan/GitRepos/LogMining/data/input'

    ReadAllFilesInDirectory(targetDirPath)
