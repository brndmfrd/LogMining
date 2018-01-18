
"""Python 3.6.3 Anaconda."""
import os
import data.parseByTags as Pt
import data.loadOneDay as LoadOneDay
import pandas as Pd
import matplotlib.pyplot as plt


class Trial1Pipeline:
    """DocString."""

    def __init__(self, inputDirPath):
        """DocString."""
        self.inputDataFilePath = inputDirPath

        """Construct where the final report data goes for Trial 1"""
        self.currFileLoc = os.path.abspath(os.path.dirname(__file__))
        self.reportFileRelPos = r'/trials/trial_1'
        self.reportFilePath = self.currFileLoc + self.reportFileRelPos

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

        # Read and process data.
        allTheSegments = self.GetDataSegments()

        # Prettiefy our data for printing.
        dataframe = self.PrettyPrint(allTheSegments)

        # Generate Stats.
        self.GenerateStats(dataframe)

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

            # This does the heart of the processing.
            segmentData = Pt.ParseMap(rawData)
            return segmentData

    @classmethod
    def PrettyPrint(cls, allTheSegments):
        """ Pretty print our processed data. """
        df = Pd.DataFrame(allTheSegments)
        df = df.transpose()
        df.columns = ['DEBUG', 'VERBOSE', 'INFO', 'WARN', 'ERROR', 'FATAL', ]
        with Pd.option_context('display.max_rows',
                               None,
                               'display.max_columns',
                               6):
            print(df)

        return df

    def GenerateStats(self, df):
        """Initialy we will just print the stat out to the console.
           We can deal with files and dirs later. TODO.
           Argument df is our input dataframe.
        """
        print('=============== Maximums ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].max(axis=0))

        print('=============== Minimums ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].min(axis=0))

        print('=============== Mean (arithmatic) ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].mean(axis=0))

        print('=============== Median ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].median(axis=0))

        print('=============== Sum ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].sum(axis=0))

        print('=============== Std ===============')
        for elem in df.columns:
            print(elem)
            print(df.loc[:, elem].std(axis=0))

        print('=============== Correlation ===============')
        print(df.corr('pearson', 1))

        # Plotting
        for elem in df.columns:
            df[[elem]].plot()

        df[['WARN', 'ERROR', 'FATAL']].plot(label='Danger Logs')
        plt.show()
