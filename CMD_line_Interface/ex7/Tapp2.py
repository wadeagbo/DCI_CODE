import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser(description="Data information")
 
# Adding optional argument
parser.add_argument("-n1", "--name1", type=str, help = "Your firstame:  ")
parser.add_argument("-n2", "--name2", type=str, help = "Your lastname:  ")
parser.add_argument("-yr", "--age", type=int,   help = "Your Age: ")
parser.add_argument("-f", "--fast", action='store_true', help = "Fast mode enabled")

 
# Read arguments from command line
args = parser.parse_args()
 
if args.age==None:
    args.age=100


elif args.name2==None:
    args.name2= 'Hanson'


elif args.name1==None:
    args.name1= 'Larry'
else:
    print("%s :  Fast mode enabled" %args.fast)

print("FIRST_NAME:  % s" % args.name1)
print("LAST_NAME: % s" % args.name2)
print("AGE: % s" % args.age)
print("Hello  %s  %s"  % (args.name1, args.name2) )
print("I see that you have had %s birthdays." % (args.age+1))
