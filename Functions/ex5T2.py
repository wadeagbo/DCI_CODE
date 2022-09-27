first_name =""    #global variable

def full_name():
    first_name " Peer"   # local variable with locasl scope
    last_name= ""
    return f"{first_name} {last_name}"

print(full_name())
