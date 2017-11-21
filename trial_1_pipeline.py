import data.parseByTags as Pt
import data.loadOneDay as LoadOneDay
import pandas as Pd



class Trial1Pipeline:	
    def __init__(self, inputDirPath):
        self.inputDataFilePath = inputDirPath
        print('INIT Trial1Pipeline')
        
        
    def __enter__(self):
        return self

        
    '''
    Still trying to understand how to correctly use this method.
    '''
    def __exit__(self, exc_type, exc_value, traceback):
        #print(exc_type)
        #print(exc_value)
        isinstance(exc_value, TypeError)
        
          
    def Pipeline(self):
        print('--Start pipeline--')
        
        allTheSegments = []
        
        with LoadOneDay.LoadOneDay(self.inputDataFilePath) as Loader:
            rawData = Loader.ReadAllFilesInDirectory()
            print( len(rawData) )
            allTheSegments = Pt.ParseMap(rawData)
            
        # Pretty print the data in the way we should conceptualize it.        
        # for i in allTheSegments:
            # outst = str(i).ljust(8) + ''.join([str(x).ljust(8) for x in allTheSegments[i]]) + '\n'
            # print(outst)
        
        df = Pd.DataFrame(allTheSegments)
        df = df.transpose()
        df.columns = ['DEBUG','VERBOSE','INFO','WARN','ERROR','FATAL',]
        with Pd.option_context('display.max_rows', None, 'display.max_columns', 6):
            print(df)
            
        print('--End pipeline--')
        
        return True