# LogMining
A project structured to contain a variety of scripts for mining log data both generally and ad-hoc.

Python v3.4.5
R v3.3.2



# Directory Structure

*bin/
	Binarys are kept here. These binaries are designed strictly to do processing. Any sanitizing, parsing, presenging graphical output should be done in the utilities (util/) directory. These binaries are aware of their relative location in the directory structure.

*docs/
	Documentation explaining anything and everything from how to set up and work in this environment to the specifications of what technology is used to explanations of each binary and the purpose of what it achives. 

*util/ 
      Utility binaries. These are scripts and other tools that perform data sanatization, parsing, and create graphs out of structured data. These tools are designed to be generic for reusability.

*data/
	This directory contains both the input and output files (raw form) to be processed. The input files are not to be modified by any process. In this direcotry is a temporary location for raw input that has been modified, but not yet ready to be disposed and will be used for further processing to generate new output. The output should be well structured and useful for any graphical output or analysis.

*reports/
	Reports on data analysis. These reports outline what was expected, what processes ran (and how to recreate the raw data and output), what graphs are used, what binaries are used, and contrast what was expected with what was discovered and any further implications or curiosities.