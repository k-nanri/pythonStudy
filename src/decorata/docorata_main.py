from collections.abc import Callable
import functools

"""
デコレータにする関数を宣言
パラメータはそのままデコレータのパラメータになる
"""
def calling_tax(name: str) -> Callable:
    """
    内部関数を宣言。パラメータはCallable
    このCallableは、デコレータを設定した関数が設定される
    """
    def _calling_tax(func: Callable):
        """
        _wrapper関数内で処理を実行
        *args、**kwargsがデコレータを付与した関数のパラメータの値が設定される
        """
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            print("calling_tax decorator start ------>")
            print("name = " + name)
            print("args = " + str(args))
            func(*args, **kwargs)
            print("-------> calling_tax decorator end")
        return _wrapper
    return _calling_tax


"""
デコレータにする関数を宣言。パラメータはCallable
"""
def calling(func: Callable) -> Callable:
    """
    _wrapper関数を宣言。パラメータは*argsと**kwargs
    デコレータを付与した関数のパラメータが設定される。
    """
    def _wrapper(*args, **kwargs):
        print("calling decorator start ------->")
        print("args = " + str(args))
        # デコレータを付与した関数を実行
        func(*args, **kwargs)
        print("---------> calling decorator end")

    return _wrapper

@calling_tax("watanabe")
def execute_tax(address: str, tel: int):
    print("start execute_tax")
    print("address = " + str(address))
    print("tel     = " + str(tel))


@calling
def execute(name: str, age: int):
    print("execute start")

if __name__ == '__main__':
    execute("tanaka", 20)
    #execute_tax("Kanagawa", 11111)