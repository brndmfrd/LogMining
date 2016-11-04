Tag parser is used to parse out tags in logs (e.g. [WARN], [DEBUG]).

Assumption: 
    These are the only log tags: VERBOSE, TRACE, DEBUG, WARN, ERROR, FATAL
    (TODO: add these into a config file that the parser can read and match)
    
The result of executing this script is a stripped down representation of the same log file, but with all data removed and the tags added with a single character representation. 

Tags are mapped as such: 
    VERBOSE -> V
    TRACE -> T
    DEBUG -> D
    WARN -> W
    ERROR -> E
    FATAL -> F
    (todo: these mappings should be in a config file.)
    (Note! These mappings must be unique. You must not have two logs map to the same letter.)
    
example:
    January 25, 1996: Somepath.Someclass [WARN] ...
    =>
    W
    
    
Useful when finding log level patterns and counting number of each type of log entry in a given logfile.