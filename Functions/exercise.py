def full_name(*args): # "tupl"
    # 2 names, 3 etc.
    # Handle it "gracefully!!"
    # print(args)
    # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
    # --> TUPLE / List (Tuples cannot be changed/mutated )
    return args

# looping crash
names = ('Felipe', 'Gonzalez') ## tuple

# 2 major ways of doing it
full_string = ""
for name in names:
    full_string += f"{name} " # name + " " $$$
    # print(name, end="") # A for effort!!!

print(full_string.strip())    
