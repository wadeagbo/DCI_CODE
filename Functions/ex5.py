#*args! (**kwargs)
#date structure ---called a dictionary


# English top German

# Guten Tag - Good day

greetings= {
        "key":"value", 
        "table": "a place to put your food on", 
        "car": "a machine to help a humna move from one place to another"}

greetings["table"]



def  full_namne(**kwargs):
    print(kwargs)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f" {first_name} {last_name}"


#howw to use it


print (full_name(first_name(first_name=input('What is your first name?') ))
