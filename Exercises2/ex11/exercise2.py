"""
# replace() in python

## Overview:

The replace() method replaces each substring of a string that matches the given string. 

## Task

Write a program that replaces the standalone "dog" in the following sentence with "cat".
Use f-string when printing the output.

## Input/Output
```
"A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."  -->  "Output: A dogmatic cat buys dogecoin to become rich and buy hotdogs every day."
```
"""



new_word =" "
word= "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day." 
for each_element in word.split():
    if each_element=='dog':
        each_element="cat"
    new_word +=each_element+" " 
    
print(new_word)
 
