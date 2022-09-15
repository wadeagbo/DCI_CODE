import re


### Read in the text file

with open('data.txt', 'r',encoding='utf-8') as f:
    contents = f.read()


#### pattern
    pattern = re.compile(r'\w+@\w+.\w+')


    matches=pattern.finditer(contents)

### search with loop
    for match in matches:
        print(match)

print()


##### Alternatively 

pattern1 = "\w+@\w+.\w+"
print(re.findall(pattern1,contents))

