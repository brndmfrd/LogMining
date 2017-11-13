import data.parseByTags as PBT

#PBT.testfunction()

class Trial1Pipeline:
    classValue = 1
	
    def __init__(self):
        self.classValue = 99999

    def __enter__(self):
        return self

    '''
    Still trying to understand how to correctly use this method.
    '''
    def __exit__(self, exc_type, exc_value, traceback):
        #print(exc_type)
        #print(exc_value)
        isinstance(exc_value, TypeError)
	
    def testprint(self):
        print('it works')
        return self.classValue