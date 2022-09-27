with open(filename, "w") as file:
    for key, value in kwargs.items():
        file.write("{}: {}\n".format(key, value))



kwargs = {'page': 1, 'name': 'xyz', 'title': 'xyz'}
