from functools import lru_cache

@lru_cache(maxsize=2)
def again():
    print("hoge")
    r = 0
    for i in range(100000000):
        r += i

    return r

def main_call():
    for i in range(5):
        print(again())
        print(again.cache_info())

if __name__ == '__main__':
    main_call()


