def full_name(*args):  # tuple
    print(args)
    return f"{args[0]} {args[1]}"
  
print(full_name("felipe", "Gonzalez", "Pedro")) 
