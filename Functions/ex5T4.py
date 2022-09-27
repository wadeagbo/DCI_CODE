last_name = ["Doe"]
# "Pass by reference" variables can change
def full_name(last_name):
    # variations 
    last_name[0] = "Hoffmann"
    return last_name


print(last_name)

full_name(last_name)
print(full_name(last_name))

print(last_name)
