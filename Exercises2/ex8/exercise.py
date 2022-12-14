"""
# find in Python

## Task - Finding Nemo

You need to find the word "Nemo" in a given string and return its position in that string, like this:

```
I found Nemo at [index]!
```

If you can't find Nemo, return:

```
I can't find Nemo :("
```

## Examples:
```
"I am finding Nemo !"  -->    "I found Nemo at 13!"  
"Nemo is me"           -->    "I found Nemo at 0!"  
"I Nemo am"            -->    "I found Nemo at 2!"  
"Hello World"          -->    "I can't find Nemo :("  
```

"""



string_set = ["I am finding Nemo !", "Nemo is me" , "I Nemo am", "Hello World"]
for eachstr in string_set:
    nfind= eachstr.find("Nemo")
    if  nfind >=0:
        print(f"I found Nemo at  {nfind}!")
    else:
        print(f"I can't find Nemo :( " )
