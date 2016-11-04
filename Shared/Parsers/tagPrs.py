import sys
import os
import re


def main():
    expr = re.compile(r"(\[VERBOSE\]|\[TRACE\]|\[DEBUG\]|\[INFO\]|\[WARN\]|\[ERROR\]|\[FATAL\])")
    somestring = r"alphabet[TRACE]soup"

    myMatch = expr.search(somestring)

    if(myMatch):
        print (myMatch.group())
    else:
        print ("No match!")
    
    print ("--DoneonRings--") 



if __name__ == "__main__":
    absPathFileToParse = ""

    if len(sys.argv) != 2:
        print ("Absolute path to file name required as argument.")
    else:
        absPathFileToParse = sys.argv[1]

    print ("Begin parseing file: " + absPathFileToParse)
    
    main()
