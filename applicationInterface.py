#!python3.6
import applicationConfiguration as appConfig
import trial_1_pipeline


'''
Single interface for a user to call the separate trials and to re-use data in multiple trials if desired.
The user selects which trial they want to run and the necessary pipeline is called for that trial.
e.g. 
user selects trial 1
data is read for trial 1 
...     
'''
def StartTrial1():
    print('StartTrial1')
    with trial_1_pipeline.Trial1Pipeline() as Trial1:
        result = Trial1.testprint()
        print('result ' + str(result))


def BeginTrialSelectionLoop():
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


