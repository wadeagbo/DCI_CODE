"""
# substring in Python

## Overview:

The python string[start: end: step] method returns a part of the string.
We pass start index and end index number position where both start and end index is exclusive.

## Task

### "Without own words"
Please write a program that prints out "Hello Gregor". The challenge is that you are not allowed to create own chars & strings. You are only allowed to use elements of a given string provided in the solution.py file.


### Output
```
"Hello Gregor"

"""


given_string = """One morning, when Gregor Samsa woke from troubled dreams,
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a
little he could see his brown belly, slightly domed and divided by
arches into stiff sections. The bedding was hardly able to cover
it and seemed ready to slide off any moment. His many legs, pitifully
thin compared with the size of the rest of him, waved about helplessly
as he looked."""

ns= len(given_string)

#word1= "hello"
#word2= "Gregor"
#word3 = "waheed"

def select_word(word,given_string):
    greet =word
    ng= len(greet)
    greet_new =""
    num1 =""
    for char1 in greet:
        for char2 in given_string:
            if char2==char1:
                greet_new +=char2
                num = given_string.index(char2)
        num1  += given_string[num]
        print(f"{given_string[num] :>10}     [{num :2}] " )
    return num1


word1 = input(" input search word 1 in the string:   ")
word2 = input(" input search word 2 in the string:   ")
print()
string1 = select_word(word1,given_string)
print()
string2 = select_word(word2,given_string)
print()
print(f"        {string1} {string2} ")
print()

