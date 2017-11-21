#!python3.6
import os
#import applicationConfiguration as appConfig
import trial_1_pipeline

'''
Main routine: BeginTrialSelectionLoop
Extending: 
    Add new trial in trials directory
    Add new dictionary reference in BeginTrialSelectionLoop() dictionary 'trialDict'
    Add new method here referenced by new entry in 'trialDict'
    Add new pipeline script e.g. 'trial_1_pipeline.py' in the same directory
        Pipeline gets data and target trial
        Produces report
        Is disposable
'''

applicationLocation = os.path.abspath(os.path.dirname(__file__))

'''
Single interface for a user to call the separate trials and to re-use data in multiple trials if desired.
The user selects which trial they want to run and the necessary pipeline is called for that trial.
e.g. trial_1_pipeline
user selects trial 1
data is read for trial 1 
...     
'''
def StartTrial1():
    print('StartTrial1')
    tempDataRelPos = r'/data/temp/'
    
    inputDataFilePath = applicationLocation + tempDataRelPos
    
    with trial_1_pipeline.Trial1Pipeline(inputDataFilePath) as Trial1:
        result = Trial1.Pipeline()


def BeginTrialSelectionLoop():
    # When you add more trials, extend this dictionary!!
    trialDict = {
        1:StartTrial1
    }
	
    keepGoing = 'y'

    while(keepGoing.upper() == 'Y'):
        selection = input('Please select which trial you would like to run [1-9]+\t\n')
        if int(selection) > 0 and int(selection) <= len(trialDict):
            trialDict[int(int(selection))]()
        keepGoing = input('Run a new Trial? [Y/any]')


def Main():
    BeginTrialSelectionLoop()


if __name__ == '__main__':
    Main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

