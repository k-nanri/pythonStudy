
if __name__ == '__main__':

    # 砲丸判定(in, not in)
    list_data = ['a', 'b', 'c', 'd']
    b1 = 'a' in list_data
    print(b1)

    b2 = 'x' in list_data
    print(b2)

    b3 = 'a' not in list_data
    print(b3)

    b4 = 'x' not in list_data
    print(b4)

    list_data1 = ['a', 'b', 'c']
    list_data2 = ['d', 'e', 'f']
    new_list = list_data1 + list_data2
    print(new_list)

    text = "ABCDEFG"
    # 0番目から2番目の手前まで
    print(text[0:2])
    # 2番目から最後まで
    print(text[2:7])

    l = [1, 2, 3]
    print("len = ", len(l))

    # index
    print(l.index(2))


