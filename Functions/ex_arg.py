def full_names(*args):
    full_name =""
    for arg in args:
        full_name += f'{arg} '

    print(full_name)

full_names("A", "B", "C");
full_names("A", "B");
full_names("A");

