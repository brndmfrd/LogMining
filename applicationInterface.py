#!python3.6
import applicationConfiguration as appConfig

# Here we provide an interface to the user to interact with each of the trials. 

print(appConfig.trial1)




def BeginTrialSelectionLoop():
    keepGoing = 'y'

    while(keepGoing.upper() == 'Y'):
        selection = input('Please select which trial you would like to run [1-9]+')
        if (int)selection > 0 and (int)selection < 90:
            


def Main():
    BeginTrialSelectionLoop()


if __name__ == '__main__':
    Main()


