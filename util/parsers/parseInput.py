#!/usr/local/bin/python3.6

import sys
import os
import re

import Configurator


def Main():
    print ('main')

    
    #def ParseMap(infile):


if __name__ == "__main__":
    continueFlag = 'do not continue'

    if len(sys.argv) == 2:
        continueFlag = sys.argv[1]
    else:
        print ('This file will begin the process of parsing all files contained inside of the input directory.')
        print ('Depending on the size and quanity of the files in the input directory, this process may take a long while.')
        
        continueFlag = input('Would you like to proceed? [yes/Any]')

    if continueFlag == 'yes':
        Main()
    else:
        print (f'User input \'{continueFlag}\' does not match \'yes\'')
        print ('This script will now terminate. Toodle loo.')
