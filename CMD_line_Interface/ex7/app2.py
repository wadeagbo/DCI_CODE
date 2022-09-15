import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser(description="Data information")
 
# Adding optional argument
parser.add_argument("-n1", "--name1", type=str, help = "Your firstame:  ")
parser.add_argument("-n2", "--name2", type=str, help = "Your lastname:  ")
parser.add_argument("-yr", "--age", type=int,   help = "Your Age: ")

 
# Read arguments from command line
args = parser.parse_args()
 
if args.age==None:
    args.age=100
    print("FIRST_NAME:  % s" % args.name1)
    print("LAST_NAME: % s" % args.name2)
    print("AGE: % s" % args.age)
elif args.name2==None:
    args.name2= 'Hanson'
    print("FIRST_NAME:  % s" % args.name1)
    print("LAST_NAME: % s" % args.name2)
    print("AGE: % s" % args.age)
elif args.name1==None:
    args.name1= 'Larry'
    print("FIRST_NAME:  % s" % args.name1)
    print("LAST_NAME: % s" % args.name2)
    print("AGE: % s" % args.age)
