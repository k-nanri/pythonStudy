
x = 100

def sample_function3():
    global x
    x = 200
    print("global x = ", x)

def sample_function():
    print(x)

def sample_function2():
    x = 200
    print("x = ", x)

if __name__ == '__main__':

    sample_function()
    sample_function2()
    print("x = ", x)
    sample_function3()
    print("x = ", x)


