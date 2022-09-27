def full_names(*args):
    full_name =()
    for arg in args:
#        full_name += f'{arg} '
        full_name +=arg 
#    print(full_name)
    return  full_name

print(full_names("A", "B", "C"))
print(full_names("A", "B"))
print(full_names("A"))

