#!/usr/bin/env python3

if __name__ == '__main__':

    # 初期化
    # 0 から 5未満までの整数が格納される
    rng = range(5)
    print(rng)
    print(list(rng))

    # stopのみ
    r1 = range(5)
    print(list(r1))

    # start/stop指定
    r2 = range(1, 5)
    print(list(r2))

    # start/stop/stepまでを指定
    r3 = range(1, 5, 2)
    print(list(r3))

    for i in range(0, 10):
        print("loop = ", i)


