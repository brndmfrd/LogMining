import Configurator


# In: Name of the input file to be used for processing
# Out: Full path names for the input and output files.
# Intent: A quick default configuration that will find the input file
#   and write an output file to temp/ 
def Setup(infile):
    outfile = f"{infile}.out"

    print (f"Proceeding with filename {infile} as input.")
    print (f"Proceeding with filename {outfile} as output.")
    
    configDict = Configurator.SetConfigurations(['input', 'temp'])

    inpath = configDict['input']
    outpath = configDict['temp']

    print (f'Using input directory: {inpath}')
    print (f'Using output directory: {outpath}')

    if len(inpath)<=0 or len(outpath)<=0:
        print (f'inpath or outpath could not be determined. Please ensure this script is being ran from inside the project directory structure. This process will now terminate.')
        return

    inFileNamePath = inpath + infile
    outFileNamePath = outpath + outfile

    print (f'Using input full filename path: {inFileNamePath}')
    print (f'Using output full filename path: {outFileNamePath}')
    
    return inFileNamePath, outFileNamePath
