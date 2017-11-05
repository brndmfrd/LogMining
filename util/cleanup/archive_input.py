#!/usr/local/bin/python3.6

import terminator
import configurator

'''
Design:
Will look to the input directory and compress all files contained within and store the compressed files into the archive directory.

Expected input file:
LogMining/data/input

Expected archive directory:
LogMining/data/archive

After archiving is sucessful the input directory is purged.
'''






if __name__ == "__main__":
    if len(sys.argv) == 2:
        Main(sys.argv[1])
    else:
        print ('You must specify the name of the archive file.')
