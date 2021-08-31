
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
    
    # Union
    s1 = {'A', 'B', 'C'}
    s2 = {'C', 'D', 'E'}
    s = s1.union(s2)
    print("Union")
    print("s = ", s)
    print("s1 = ", s1)

    # Intersection (積集合)
    s = s1.intersection(s2)
    print("Intersection")
    print("s = ", s)

    # Difference (差集合)
    s = s1.difference(s2)
    print("Difference")
    print("s = ", s)

    # 含まれているかどうかを判定
    s1 = {'A', 'B'}
    s2 = {'A', 'B', 'C'}
    print("issubet = ", s1.issubset(s2))

    # 含んでいるかどうかを判定
    s1 = {'A', 'B', 'C'}
    s2 = {'A', 'B'}
    # s1がs2を含んでいるか？
    print("issuperset = ", s1.issuperset(s2))

    





