# Demonstration of class variables and instance variables

class Demo:
    # Class (static) variables
    a = 10
    b = 20


def main():
    # Accessing class variables using class name
    print(Demo.a)   # 10
    print(Demo.b)   # 20

    # Modifying class variables using class name
    Demo.a = 40
    Demo.b = 30

    print(Demo.a)   # 40
    print(Demo.b)   # 30

    # Creating an object
    d = Demo()

    # Accessing class variables through object
    print(d.a, d.b)   # 40 30

    # Creating instance variables (shadows class variables)
    d.a = 1000
    d.b = 2000

    print(d.a)   # 1000 (instance variable)
    print(d.b)   # 2000 (instance variable)

    # Class variables remain unchanged
    print(Demo.a)   # 40
    print(Demo.b)   # 30
