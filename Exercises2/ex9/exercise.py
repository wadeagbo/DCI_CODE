"""
# CAPS LOCK DAY is over!

## Task
October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end. Each string is a normalized sentence and should start with an uppercase character.

## Input/Output
```
normalize("CAPS LOCK DAY IS OVER")                -->   "Caps lock day is over!"  
normalize("Today is not caps lock day.")          -->   "Today is not caps lock day."  
normalize("Let us stay calm, no need to panic.")  -->   "Let us stay calm, no need to panic."  
```
"""

#"CAPS LOCK DAY IS OVER", "Today is not caps lock day.", "Let us stay calm, no need to panic."


string_oct={"CAPS LOCK DAY IS OVER","Today is not caps lock day.", "Let us stay calm, no need to panic."}


def Oct_str(word):
    if word.isupper():
        print(f"{word.capitalize()}!")
    else:
        print(f"{word.capitalize()}")


for each_word in string_oct:
              Oct_str(each_word)

