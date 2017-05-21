import os
import json



# Set the configurations to be used by the process.
# It is assumed that this script lives inside the project directory.
# It is assumed that the path to the cofiguration file has not changed.
# It is assumed that the paths contained in the dirpaths.conf file are updated and 
#   reflect the current project directory structure.
def SetConfigurations(targetDirs):
    # This script will need to have awareness of the project directory sctructure
    # With these two constants, we provide the full path to the file that contains the 
    # directory structure paths.
    PROJNAME = 'LogMining'
    DIRPATHCONF = PROJNAME + '/conf/dirpaths.conf'

    cwd = os.getcwd()
    projdir = cwd.split(PROJNAME, 1)[0]
    confFilePath = os.path.join(projdir, DIRPATHCONF)
    confDict = json.load(open(confFilePath, 'r'))

    dirpList = {}

    for tdir in targetDirs:
        dirpList[tdir] = projdir + confDict.get(tdir)

    return dirpList
