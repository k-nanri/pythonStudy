
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
    