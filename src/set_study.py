
if __name__ == '__main__':

    # setの初期化
    s = {'A', 'B', 'C'}
    print(s)

    # 初期化字に重複があっても
    s = {'A', 'B', 'C', 'A'}
    print(s)

    # listからsetを生成する
    l = ['a', 'b', 'c', 'a']
    print("l = ", l)
    s = set(l)
    print("s = ", s)

    data_set = {'a', 'b', 'c'}
    for s in data_set:
        print(s)

    # 要素の追加
    print("Add item")
    s = {1, 2, 3}
    print("s = ", s)
    s.add(4)
    print("s = ", s)

    # 要素の削除
    s = {1, 2, 3, 4}
    print("Remove item")
    print("s = ", s)
    s.remove(4)
    print("s = ", s)

    try:
        s.remove(99)
    except KeyError as e:
        print(e)

    # discardだとエラーは発生しない
    s.discard(99)
    print(s)

    # frozensetはイミュータブルなset
    fs = frozenset(['a', 'b', 'c'])
    print("fs = ", fs)
    for item in fs:
        print(item)
    
