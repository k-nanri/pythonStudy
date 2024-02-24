from functools import lru_cache

@lru_cache(maxsize=2)
def calculate(a):
    print("-- Call calculate function")
    r = 0
    for i in range(10000000):
        r += i

    return r

def main_call():

    print("calculate 1")
    calculate(1)
    print(calculate.cache_info())

    print("calculate 2")
    calculate(2)
    print(calculate.cache_info())

    print("cacheが効いているはず -------")
    print("calculate 1")
    calculate(1)
    print(calculate.cache_info())

    print("calculate 2")
    calculate(2)
    print(calculate.cache_info())

    print("1のキャッシュが削除 -------")
    print("calculate 3")
    calculate(3)
    print(calculate.cache_info())

    print("2と3のcacheが効いているはず -------")
    print("calculate 2")
    calculate(2)
    print(calculate.cache_info())

    print("calculate 3")
    calculate(3)
    print(calculate.cache_info())

    print("1のcacheがない -------")
    print("calculate 1")
    calculate(1)
    print(calculate.cache_info())

if __name__ == '__main__':
    main_call()


