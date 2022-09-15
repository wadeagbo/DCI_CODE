import getopt, sys
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hfs:"
 
# Long options
long_options = ["Help", "fast", "slow="]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help for either fast of slow mode")
             
        elif currentArgument in ("-f", "--fast"):
            print ("fast mode enabled", sys.argv[1])
             
        else :
            print ("slow mode enabled")
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
