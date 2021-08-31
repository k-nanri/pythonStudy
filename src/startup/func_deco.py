
def deco_func(f):
    
    def new_func(*args, **kwargs):
        print("start")
        val = f(*args, **kwargs)
        print(val)
        print("end")

    return new_func

@deco_func
def my_func(n, m):

    ret = 0
    for i in range(n, m+1):
        ret += i

    return ret

if __name__ == '__main__':

    """
    f = my_func
    new_func = deco_func(f)
    new_func()
    """
    my_func(1, 10)

