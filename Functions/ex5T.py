greetings = {
    "key": "value",
    "table": "a place to put your food on",
    "car": "a machine to help a human move from one place to another"
}


def full_name(*args, **kwargs): # kwargs are DICTIONARIES
    print('--kwargs: ->', kwargs)
    print('---args: ->', args)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{args[0]} {first_name} {last_name}"

# how to use it!
print(full_name('Good morning', first_name='Jane', last_name='Doe', location="Berlin"))
