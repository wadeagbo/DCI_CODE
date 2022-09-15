import re

with open("klog.txt", "r") as file:
	text = file.read()

pattern = r"\w+@\w+.\w{1,3}"

match = re.search(pattern,text)

print(match)


#--------------------------

print()
print()
print()



pattern2 = r"\[(.*)\]"

match2 = re.split(pattern2,text)

print(match2)

for i in match2:
	print(i)


