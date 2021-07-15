
if __name__ == '__main__':

    # 数値のリスト
    l1 = [1, 3, 5, 7, 9]
    # 文字列のリスト
    l2 = ['pen', 'pineapple', 'apple', 'pen']
    # 型の異なるリスト
    l3 = [1, 'pen', l1, l2]
    l4 = []

    print(l1)
    print(l2)

    l1 = [1, 2, 3]
    l2 = list(l1)

    print(l1)
    print(l2)

    l1 = [1, 2, 3, 4, 5]
    print(l1[0])
    print(l1[1])
    print(l1[2])

    print(l1[-1])
    print(l1[-4])
    print(l1[-5])

    l2 = ['a', 'b', 'c' , 'd', 'e']
    print(l2[0:1])
    print(l2[0:2])
    print(l2[1:4])
    print(l2[0:-1])
    print(l2[0:])
    print(l2[:99])

    print(len(l2))
    print(l2[len(l2) - 1])


    l = [1, 2, 3, 4, 0]
    l[0] = 99
    print("l = ", l)

    # Add Value
    l.append(10)
    print(l)

    # Insert
    # index number is 0
    l.insert(0, 80)
    print(l)

    # index number is 2
    l.insert(2, 70)
    print(l)

    # last (末尾に追加ではない)
    l.insert(-1, 100)
    print(l)

    l.remove(100)
    print(l)

    try:
        l.remove(100)
    except Exception as e:
        print(e)

    l = ['a', 'b', 'c', 'd']

    del l[2]
    print(l)

    l = ['a', 'b', 'c', 'd']
    del l[-1]
    print(l)

    l = ['a', 'b', 'c', 'd']
    del l[0:2]
    print(l)

    l = ['a', 'b', 'c', 'd']
    x = l.pop(2)
    print(x)
    print(l)

    



    