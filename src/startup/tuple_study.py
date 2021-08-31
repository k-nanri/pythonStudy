#!/usr/bin/env python3

if __name__ == '__main__':

    # タプルは一度初期化すると要素の更新ができない

    # 要素なし
    t1 = ()
    print(t1)

    # 要素が１つのときのはカンマはつけない
    t2 = (1)
    print(t2)
    t2 = (1,)
    print(t2)

    # カンマ区切りで複数の要素をセットする
    t3 = ('a', 'b', 'c')
    print(t3)

    # list から tuple に変換
    l = [1, 2, 3]
    t = tuple(l)
    print(t)


    


