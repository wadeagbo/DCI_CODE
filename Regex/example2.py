  
import re

text = """Hey Mr. Bezos,
I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 
therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com
Let me give you for some reason also your most important passwords to continue running amazon! Sorry Im new at this job.
epsteindidntkillhimself14141
ThIs1s4ctua11YaG00dPa$$w0rD
123456seven
password
Kind regards,
the soon to be fired secretary Tanisha"""


 

#user_input = input()

user_input = text
#pattern=  r'[a-zA-Z0-9]+@[a-zA-Z]\.(com|edu|net)'
pattern = r'[\w.+-]+@[\w+-]+\.[\w.-]+'

if(re.findall(pattern, user_input)):
    print("valid email")
    match = re.findall(pattern, user_input)
    print(match)
else:
    print("invalid email")


#match = re.findall(r'[\w.+-]+@[\w+-]+\.[\w.-]+', text)
#print(match)



f=text 
rx = re.compile(r'[:; ]') 
rx_email = re.compile(r'\S+@\S+\.\S+$')  
#with open(text, "r") as f:

for line in f: 
    fields = rx.split(line) 
    email = '' 
    id = '' 
    for field in fields: 
        if rx_email.match(field): 
            email = field 
        elif field != fields[-1]: 
            id = field 
    password = fields[-1] 
    print("Username: '{}', email: '{}', password: '{}'".format(id, email, password))




# Replace part of the string
#pattern1 = "(d\d\d)-(d\d\d)-(\d\d\d\d)"
#new_pattern= r"\1\2\3"
#user_input = input("Something:    ")
#new_user_input =re.sub(pattern1, new_pattern, user_input)
#print(new_pattern)

