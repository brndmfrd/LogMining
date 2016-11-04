import sys
import os
import re


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



if __name__ == "__main__":
    infile = ""

    if len(sys.argv) != 2:
        print ("Absolute path to file name required as argument.")
    else:
        infile = sys.argv[1]
 
    cwd = os.path.dirname(__file__)
    inpath = os.path.join(cwd, infile)    
    outpath = infile + ".X"

    print ("Begin parseing file: " + inpath)
    print ("Output to file: " + outpath)
    
    main(inpath, outpath)
