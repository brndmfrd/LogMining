=======================================================
Tags By Time - File Parser

(tagsByTimeFileParse.py
=======================================================
This file was designed to look into the input file directory and parse out a SINGLE FILE for it's log tags (see "Target file structure" below).
The result is a table of values that represent a day broken into ten-minute segments and a multi-space separated values, each column representing the count of 
one of the tags.

e.g. 
1  12   4  
2  11   4
3  9    12

In the above example the first column represents the first, second, and third ten-minute periods of a day.
The first column values may represent the count of DEBUG logs that were counted that were logged during each corisponding period of time.
The second column values may represent the count of ERROR logs that were counted that were logged during each corisponding period of time.
Example target from log file: [2015-09-20T19:59:24.5499068-04:00] [DEBUG]

=======================================================
Command Line Arguments
=======================================================
The name of the target input file can be provided as a command line argument. If this is done the 'defaultConfig.py' file is included.
This allows for the command line argument to be a single file name, not a full path, as the default config will search for the matching file 
name inside of the data input directory.

If no input parameter is given the script will not run.

This file is also designed to be included in other files. By calling the methods in this file other scripts can take advantage of the 
file parsing routines inside of this file.



=======================================================
Target file structure
=======================================================
Logs tags include:
     VERBOSE
     TRACE
     DEBUG
     WARN
     ERROR
     FATAL 

It is to be assumed a standard structure persists in the logs files. 
The structure of each log file cosists of 
    Each new line is a new record
    Each line contains a tag (VERBOSE, ..., FATAL)
    Each line contains a timestamp    
    



