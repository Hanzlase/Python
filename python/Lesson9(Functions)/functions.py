def hello():
    print("Hello")


hello()


def add1(num1, num2):
    print(num1 + num2)


add1(10, 20)


def add2(num1, num2):
    num1 = input("enter num1")
    num2 = input("enter num2")
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Hanzla", "john")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Hanzla", last="Sabir")
