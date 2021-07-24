
def param_func():
    return 'sample'

def sample_function1(f):
    x = f()
    print("x = ", x)

def sample_function():
    text = 'sample'
    print("text = ", text)
    return '戻り値'

if __name__ == '__main__':

    text = sample_function()
    print("text = ", text)

    f = sample_function
    text = f()
    print("text = ", text)

    sample_function1(param_func)

