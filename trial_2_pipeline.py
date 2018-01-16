
"""Python 3.6.3 Anaconda."""
import data.parseByTags as Pt
import data.loadOneDay as LoadOneDay
import pandas as Pd


class Trial2Pipeline:
    """DocString."""

    def __init__(self, inputDirPath):
        """DocString."""
        self.inputDataFilePath = inputDirPath
        print('INIT Trial2Pipeline')

    def __enter__(self):
        """DocString."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """DocString."""
        # print(exc_type)
        # print(exc_value)
        isinstance(exc_value, TypeError)

    def Pipeline(self):
        """DocString."""
        print('--Start pipeline--')

        """ Read and process data. """
        allTheSegments = self.GetDataSegments()

        """Prettiefy our data for printing."""
        self.PrettyPrint(allTheSegments)

        print('--End pipeline--')

        return True

    def GetDataSegments(self):
        """ Generate context for reading and parsing file.
            Cleanup after parsing & mapping as not to tie up memory.
        """
        with LoadOneDay.LoadOneDay(self.inputDataFilePath) as Loader:
            print('--BEGIN` read files from ' +
                  self.inputDataFilePath + ' --')

            rawData = Loader.ReadAllFilesInDirectory()

            print('--COMPLETE read files from ' +
                  self.inputDataFilePath + ' --')

            """ This does the heart of the processing. """
            segmentData = Pt.ParseMap(rawData)
            return segmentData

    def PrettyPrint(self, allTheSegments):
        """ Pretty print our processed data. """
        df = Pd.DataFrame(allTheSegments)
        df = df.transpose()
        df.columns = ['DEBUG', 'VERBOSE', 'INFO', 'WARN', 'ERROR', 'FATAL', ]
        with Pd.option_context('display.max_rows',
                               None,
                               'display.max_columns',
                               6):
            print(df)
