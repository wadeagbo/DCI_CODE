import re
 
pattern ='string'


String1 ='''We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''

String2 ='''string We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''


print()
print()
print()
print()


# Use of re.search() Method
print("search result:   ",re.search(pattern, String1, re.IGNORECASE))

# Use of re.match() Method
print("match result:    ",re.match(pattern, String1, re.IGNORECASE))


print()
print()
print()
print()


# Use of re.search() Method
print("search result:   "    , re.search(pattern, String2, re.IGNORECASE))

# Use of re.match() Method
print("match result:    ",re.match(pattern, String2, re.IGNORECASE))

print()
print()
print()
print()


