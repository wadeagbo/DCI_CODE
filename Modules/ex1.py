import sys
import getopt

def full_name():
    first_name = None
    last_name = None
  
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "f:l:")
      
    except:
        print("Error")
  
    for opt, arg in opts:
        if opt in ['-f']:
            first_name = arg
        elif opt in ['-l']:
            last_name = arg
      
  
    #print(first_name + " " + last_name)
    print(f"{first_name}   {last_name}")

full_name()    
