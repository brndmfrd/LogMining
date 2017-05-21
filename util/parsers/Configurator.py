import os
import json
import sys


# Sets the configurations to be used by the process.
# It is assumed that this script lives inside the project directory.
# It is assumed that the paths contained in the dirpaths.conf file are updated and 
#   reflect the current project directory structure.
# Input: List of target directory names. These are they key-values in the config file.
# Output: Full path names to the requested directories.
def SetConfigurations(targetDirs):
    # With these two holy constants, we derive the full path to all requested target directories in the project.
    PROJROOT = 'LogMining/'
    DIRPATHCONF = 'conf/dirpaths.conf'

    # Get the path for where this file lives.
    cwd = sys.argv[0]
    cwd = os.path.abspath(cwd)

    # Since this file lives in the project dir structure,
    #   we trim the path to the project root
    projdir = cwd.split(PROJROOT, 1)[0] + PROJROOT

    # The path to the config directory must match the path what we have listed here in this module.
    confFilePath = os.path.join(projdir, DIRPATHCONF)

    # Open our config file. Config data is structured as json
    confDict = json.load(open(confFilePath, 'r'))
    
    dirpList = {}

    # For every target directory name specified by our input params 
    #   we find the path in this project for that directory and return the full path to it.
    for tdir in targetDirs:
        dirpList[tdir] = os.path.join(projdir, confDict.get(tdir))

    return dirpList
