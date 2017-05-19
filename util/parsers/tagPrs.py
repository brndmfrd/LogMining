import sys
import os
import re


PROJNAME = 'LogMining'
DIRPATHCONF = PROJNAME + '/conf/dirpaths.conf'
inputdir = ''


def main(inpath, outpath):
    expr = re.compile(r"(\[VERBOSE\]|\[TRACE\]|\[DEBUG\]|\[INFO\]|\[WARN\]|\[ERROR\]|\[FATAL\])")
    somestring = r"alphabet[TRACE]soup"

    with open(inpath, 'r') as instream:
        with open(outpath, 'w') as outstream:
            for line in instream:
                word = expr.search(line)
                if (word):
                    outstream.write(word.group() + '\n')

    print ("--DoneonRings--") 



def GetInputDir(infile):
    cwd = os.getcwd()
    inputdir = cwd.split(PROJNAME, 1)[0]
    inpath = os.path.join(inputdir, DIRPATHCONF)
    # check if file exists
    # try to read file
    # parse json file for input dir
    # check if input dir exists
    # use file name parameter to look for file contained by input dir
    # try to read input file (permissions check)
    # work? good! not working? boo!
    

if __name__ == "__main__":
    infile = ""

    if len(sys.argv) != 2:
        print ("File name required as argument (i.e. myinputfile.txt)")
    else:
        infile = sys.argv[1]
 
    GetInputDir(infile)

    # Define output file stuff here
    outfile = infile + ".X"

    print ("Begin parseing file: " + infile)
    print ("Output to file: " + outfile)
    
    #main(inpath, outpath)
