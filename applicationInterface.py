
"""Python 3.6.3 Anaconda.

Main routine:
BeginTrialSelectionLoop
Extending:
    Add new trial in trials directory
    Add new dictionary reference in BeginTrialSelectionLoop() dictionary
        'trialDict'
    Add new method here referenced by new entry in 'trialDict'
    Add new pipeline script e.g. 'trial_1_pipeline.py' in the same directory
        Pipeline gets data and target trial
        Produces report
        Is disposable
"""

import os
import trial_1_pipeline
import trial_2_pipeline

applicationLocation = os.path.abspath(os.path.dirname(__file__))


def StartTrial1():
    """Begins trial one's pipeline and specific setup configuration."""
    print('BEGIN Trial 1')
    tempDataRelPos = r'/data/temp/'

    inputDataFilePath = applicationLocation + tempDataRelPos

    with trial_1_pipeline.Trial1Pipeline(inputDataFilePath) as Trial1:
        result = Trial1.Pipeline()
        if not result:
            print('There was a problem processing Trial 1.')
    print('END Trial 1')


def StartTrial2():
    """Begins trial two's pipeline and specific setup configuration."""
    print('BEGIN Trial 2')
    tempDataRelPos = r'/data/temp/'

    inputDataFilePath = applicationLocation + tempDataRelPos

    with trial_2_pipeline.Trial2Pipeline(inputDataFilePath) as Trial2:
        result = Trial2.Pipeline()
        if not result:
            print('There was a problem processing Trial 2.')
    print('END Trial 2')


def BeginTrialSelectionLoop():
    """Execute main work loop."""
    # When you add more trials, extend this dictionary!!
    trialDict = {
        1: StartTrial1,
        2: StartTrial2
    }

    keepGoing = 'y'

    while keepGoing.upper() == 'Y':
        selection = input('Select which trial to run [1-9]+\t\n')
        if int(selection) > 0 and int(selection) <= len(trialDict):
            trialDict[int(selection)]()
        keepGoing = input('Run a new Trial? [Y/any]')


def Main():
    """Docstring."""
    BeginTrialSelectionLoop()


if __name__ == '__main__':
    Main()
