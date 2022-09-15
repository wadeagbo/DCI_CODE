import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser(description="Data information")
 
# Adding optional argument
parser.add_argument("-n1", "--name1", type=str, help = "Your firstame:  ")
parser.add_argument("-n2", "--name2", type=str, help = "Your lastname:  ")
parser.add_argument("-yr", "--age", type=int,   help = "Your Age: ")

 
# Read arguments from command line
args = parser.parse_args()
 
#Print

print("Hello  %s  %s"  % (args.name1, args.name2) )
print("I see that you have had %s birthdays." % (args.age+1))
