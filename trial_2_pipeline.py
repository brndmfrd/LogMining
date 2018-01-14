
"""Python 3.6.3 Anaconda."""
import data.parseByTags as Pt
import data.loadOneDay as LoadOneDay
import pandas as Pd


class Trial1Pipeline:
    """DocString."""

    def __init__(self, inputDirPath):
        """DocString."""
        self.inputDataFilePath = inputDirPath
        print('INIT Trial1Pipeline')

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

        allTheSegments = self.GetDataSegments()

        """Prettiefy our data for printing."""
        df = Pd.DataFrame(allTheSegments)
        df = df.transpose()
        df.columns = ['DEBUG', 'VERBOSE', 'INFO', 'WARN', 'ERROR', 'FATAL', ]
        with Pd.option_context('display.max_rows',
                               None,
                               'display.max_columns',
                               6):
            print(df)

        print('--End pipeline--')

        return True

    def GetDataSegments(self):
        # Context for our raw data
        # Raw data access will likely change in the future (DB, HDFS, ETC)
        # Let garbage collector clean up data we temporarily hold in memory.
        with LoadOneDay.LoadOneDay(self.inputDataFilePath) as Loader:
            rawData = Loader.ReadAllFilesInDirectory()
            print('Records read from all files - ' + str(len(rawData)))
            return Pt.ParseMap(rawData)
