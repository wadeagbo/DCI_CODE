##Names, objects and mutability
def test(param1=None):
    print(id(param1))

    if not param1:
        param1 = []
        print(id(param1))

        param1.append(2)
        print(param1)

test()
test()
test()
test()
test()
test()
test()
test()

