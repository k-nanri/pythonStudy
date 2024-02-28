from collections.abc import Callable
import functools

def func_setup(name: str) -> Callable:
    def _func_setup(func: Callable):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            print("decorator start------>")
            print("name = " + name)
            print("args = " + str(args))
            print("kwargs = " + str(kwargs)
            func(*args, **kwargs)
            print("------->decorator end")
        return _wrapper
    return _func_setup


@func_setup(name="hoge")
def execute(data1):
    print("execute call!!")

if __name__ == '__main__':
    execute("test")