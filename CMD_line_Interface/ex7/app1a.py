import sys

# total number of argument
arg_len= len(sys.argv)
print("Total number of argument passed is %i" %(arg_len))

# Arguments passed

main_loop = True

while main_loop == True:

    for i in range(1,arg_len):
        if sys.argv[i] =="--help":
            print("%s  Passed arguments which is either in fast mode, or in slow mode" %(sys.argv[i]))
            main_loop = False
        elif sys.argv[i] =="--fast":
            print("%s fast mode enabled" %(sys.argv[i]))
            main_loop = False
        else:
            print("%s slow mode enabled" %(sys.argv[i]))
            main_loop = False
