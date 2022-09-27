first_name = "Jacques"
last_name  =  "Doe"

def full_name():
    last_name= "Hoffmann"

    def add_Sir(name):
        return f"Sir {name} {last_name}"


    new_full_name = add_Sir(first_name)

    return new_full_name

print(full_name())

print(first_name)

print(last_name)

