
def sample_function6():
    return 3, 'b'

def sample_function5():
    pass

def sample_function4(arg1, **arg2):
    print("arg1 = ", arg1, ", arg2 = ", arg2)

def sample_function3(arg1, *arg2):
    print("arg1 = ", arg1, ", arg2 = ", arg2)

def sample_function2(arg1, arg2='x', arg3='y'):
    print("arg1 = ", arg1, ", arg2 = ", arg2, ", arg3 = ", arg3)

def sample_function(x, y):
    z = x + y
    return z

if __name__ == '__main__':
    print("Function!!")
    z = sample_function(1, 2)
    print("z = ", z)

    sample_function2('a', 'b', 'c')
    sample_function2(arg3='c', arg2="b", arg1="a")
    sample_function2('a', arg2='b')
    sample_function2('a')

    sample_function3('a', 'b', 'c', 'd')

    sample_function4('a', key1='x', key2='y', key3='z')
    y = sample_function5()
    print("sample_function5 resutn value = ", y)
    a, b = sample_function6()
    print("a = ", a, ", b = ", b)







