import re

text= "abbys"


pattern = r"^a...s$"


match = re.match(pattern, text)

if match:
    print("successful")
else:
    print("not successful")
