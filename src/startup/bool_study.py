# bool型の勉強

if __name__ == '__main__':

    b1 = True
    b2 = False

    # 論理和
    b3 = b1 or b2
    print(b3)

    # 論理積
    b4 = b1 and b2
    print(b4)

    # 否定
    b5 = not b1
    print(b5)

    b1 = True
    b2 = False
    b3 = True

    b = b1 and b2 and b3
    print(b)

    b = b1 or b2 and b3
    print(b)

    x = 100
    y = 200
    b1 = (x < y)
    print("x < y = ", b1)

    b2 = (y < x)
    print("y < x = ", b2)

    b1 = True
    b2 = False
    print(int(b1))
    print(int(b2))

    



