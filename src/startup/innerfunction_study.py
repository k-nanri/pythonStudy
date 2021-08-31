
def outer_function2():
    """外側の関数"""
    x = 100
    print("x = ", x)

    def inner_function2():
        """内側の関数"""
        nonlocal x
        x = 200
        print("x = ", x)

    inner_function2()
    print("x = ", x)


def outer_function1():
    print("outer1")

    def innter_function1():
        print("inner1")
        
    f = innter_function1
    return f


def outer_function():
    """外側の関数"""
    print("outer")

    def inner_function():
        """内側の関数"""
        print("inner")

    inner_function()

if __name__ == '__main__':

    outer_function()
    f = outer_function1()
    f()
    outer_function2()
