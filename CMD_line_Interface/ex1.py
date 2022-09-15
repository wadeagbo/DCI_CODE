import sys

# total number of argument


n=  len(sys.argv)
print("Total arguments passed: ", n)

#Argument passed
print("Name of python script; " , sys.argv[0])

#Addition  of numners
sum_of_arguments = 0

for i in range(1,n):
    sum_of_arguments += int(sys.argv[i])

print("Result:" , sum_of_arguments)
