#Packing and unpacking arguments
 


def full_name(*arg, **kwargs):           #**   *a---takes all none takes only one letter
    first = kwargs["first"]
    last = kwargs["last"]
    return f" {arg[0]} {first} {last}"

data = {"first": "James",   
          "last": "Brown"
        }

friend = full_name("Mr" , **data)       #**   I also tried none * it works
print(friend)

