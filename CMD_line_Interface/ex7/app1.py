import sys

# total number of argument
arg_len= len(sys.argv)
print("Total number of argument passed is %i" %(arg_len))

# Arguments passed

    
for i in range(1,arg_len):
    if sys.argv[i] =="--help":
        print("%s  Passed arguments either in fast mode, or in slow mode" %(sys.argv[i]))
    elif sys.argv[i] =="--fast":
        print("%s fast mode enabled" %(sys.argv[i]))
    else:
        print("%s slow mode enabled" %(sys.argv[i]))
