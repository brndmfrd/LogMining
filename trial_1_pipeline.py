import data.parseByTags as Pt
import data.loadOneDay as LoadOneDay
from pandas import DataFrame

class Trial1Pipeline:	
    def __init__(self, inputDirPath):
        self.inputData = LoadOneDay.ReadAllFilesInDirectory(inputDirPath)
        
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
        print('--Start test--')
        print( len(self.inputData) )
        allTheSegments = Pt.ParseMap(self.inputData)
        
        
        # Pretty print the data in the way we should conceptualize it.        
        # for i in allTheSegments:
            # outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in allTheSegments[i]]) + '\n'
            # print(outst)
        
        df = DataFrame(allTheSegments)
        df = df.transpose()
        df.columns = ['DEBUG','VERBOSE','INFO','WARN','ERROR','FATAL',]
        
        print(df)
        
        print('--End test--')
                
        return True