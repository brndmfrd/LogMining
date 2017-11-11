#!python3.6
import sys, os

# Full path to the directory that contains the top-level project directory
# e.g. /home/JohnnyUser/LogMining/
# To be defined by user 
applicationLocation = '/home/bryan/GitRepos/LogMining'

# Top-level directory names
dataDir = 'data'
trialsDir = 'trials'

# Trial Paths
trial1 = os.path.abspath(os.path.join(applicationLocation, trialsDir, 'trial1.py'))
trial2 = os.path.abspath(os.path.join(applicationLocation, trialsDir, 'trial2.py'))
trial3 = os.path.abspath(os.path.join(applicationLocation, trialsDir, 'trial3.py'))
