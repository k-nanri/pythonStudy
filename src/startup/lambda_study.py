
def higher_order(datas, is_target):
    """ 高階関数のサンプル """
    for i in datas:
        if is_target(i):
            print("i = ", i)

if __name__ == '__main__':

    func = lambda x : x % 2 == 1
    is_odd = func(5)
    print(is_odd)

    is_odd = func(6)
    print(is_odd)

    datas = [1, 102, 900, 5, 3]
    higher_order(datas, lambda x : x % 2 == 1)

    func2 = lambda x,y : x + y
    result = func2(4, 5)
    print("result = ", result)
    

