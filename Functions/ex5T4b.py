last_name = {
    "key": "value",
    "table": "a place to put your food on",
    "car": "a machine to help a human move from one place to another"
}


#last_name = ["Doe"]
# "Pass by reference" variables can change


def full_name(last_name):
    # variations 
    last_name["table"] = "Hoffmann"

    return last_name

print(last_name)


full_name(last_name)
print(full_name(last_name))

print(last_name)
