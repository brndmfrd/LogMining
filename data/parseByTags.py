#!/usr/local/bin/python3.6

import re


'''
Parse structured log files by their tags. 
Return structured output; rows are ten-minute segments of a day; 
columns are the counts of each tag type.
Standalone - Reads cl-argument as input file name.
Assumption: The log data passed is all from the same day
'''
def ParseMap(logData):
    motifRgx = r'^\[[0-9]{4}\-.+?].+?]'

    # Dictionary for 10 minute segments of a given day
    tSegments = dict.fromkeys([i for i in range(144)])

    # Initialize the dictionary. The range is the number of tags we expect. 
    for i in range(len(tSegments)):
        tSegments[i] = [0 for i in range(6)]

    motifRgxC = re.compile(motifRgx)
    
    for line in logData:
        motif = motifRgxC.search(line)

        if (motif):
            # Regex for the prefix-structure of each row.
            motifsplit = re.split('\[|\]|\-|T|:|\.', motif.group())

            #year = motifsplit[1]
            #month = motifsplit[2]
            #day = motifsplit[3]
            hour = motifsplit[4]
            minute = motifsplit[5]
            #second = motifsplit[6]
            sev = motifsplit[11]
            
            # map hours to 10 minute segments
            mapHour = (int(hour) * 6)
            mapMinute = int(int(minute) / 10)
            mapTimeseg = (mapHour + mapMinute)

            # Count DEBUG - uses first letter of tag
            if sev[0] == 'D':
                tSegments[mapTimeseg][0] += 1 
                continue
                
            # Count INFO - uses first letter of tag
            if sev[0] == 'I':
                tSegments[mapTimeseg][2] += 1 
                continue
                
            # Count WARN - uses first letter of tag
            if sev[0] == 'W':
                tSegments[mapTimeseg][3] += 1 
                continue
                
            # Count ERROR - uses first letter of tag
            if sev[0] == 'E':
                tSegments[mapTimeseg][4] += 1 
                continue
                
            # Count VERBOSE - uses first letter of tag
            if sev[0] == 'V':
                tSegments[mapTimeseg][1] += 1 
                continue                
                
            # Count FATAL - uses first letter of tag
            if sev[0] == 'F':
                tSegments[mapTimeseg][5] += 1 
                continue
                
    return tSegments

'''
TODO: replace with unit test
main should only be called for demonstration or testing purposes
'''
def TestFunction():
    sampleLogs = ['[2015-09-21T00:16:27.9743119-04:00] [DEBUG] [32 ] [Tgw.Wcs.CustomLogic.Transportation.ServiceAgents.CustomLogicServiceAgent] FinishSendTask for response [Tgw.Wcs.CustomLogic.Transportation.Facade.Contracts.CheckCompletedTransportResponse]', '[2015-09-21T00:16:27.9743119-04:00] [FATAL] [3  ] [Tgw.Wcs.Transportation.Services.PointBehaviorService] LC 00004301557005267111 - After LocationBehavior in PointBehaviorService - /GapFishkill/WA1/CC01/ToAisle3Lift1SI -> /GapFishkill/WA1/CC01/Aisle3Lift1SI - bf0cb0b8-988b-49a6-90f3-0dccf4bed986.', '[2015-09-21T00:16:27.9899406-04:00] [INFO] [50 ] [Tgw.Wcs.Transportation.Services.TransportManager] LC 00004300817225365792 - In FinishTask @ taskManager!']

    tSegments = ParseMap(sampleLogs)
    for i in tSegments:
        outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in tSegments[i]]) + '\n'
        print(outst)
