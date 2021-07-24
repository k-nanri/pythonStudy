import sys
import numbers
import math

print("Hello World")


if __name__ == '__main__':

    args = sys.argv

    
    if len(args) == 1:
    
        # スクリプト名
        print(args[0])
        # 1番目の引数
        #print(args[1])
        #print(args[2])

    else:
        print('以下の形式でパラメータを指定すること')
        print('$ study.py aaa bbb')
        quit()

    a = 1
    b = 'AAA' # 文字列
    c = [1, 2, 3] # リスト
    d = {'apple': 200, 'orange': 100, 'banana': 150} # 辞書

    print(a)
    print(b)
    print(c)
    print(d)

    a = 'aaa'
    print(a)
    b = a
    print(b)

    x, y , z = 1, 2, 3
    a, b, c = x, y, z
    print(a)
    print(b)
    print(c)

    # 数値型
    bin_val = 0b0101
    print(bin_val)

    oct_val = 0o165
    print(oct_val)

    hex_val = 0xfaa
    print(hex_val)

    # float型
    x = 0.0012
    print(x)

    y = 1.2e-3
    print(y)

    # complex型
    c1 = 2 + 3j
    print(c1)
    c2 = complex(5, 6)
    print(c2)

    print(c1.real)
    print(c2.imag)

    x = 10
    y = 20
    z1 = x + y
    print(z1)

    z2 = 10 - 20
    print(z2)

    print(10 * 20)

    z3 = x / y
    print(z3)

    x = 16
    y = 3
    val = x + y
    print(val) # 19

    val = x - y
    print(val) # 13

    val = x * y
    print(val) # 48

    val = x / y
    print(val) # 5.33333333

    val = x // y
    print(val) # 5
    val = x % y
    print(val)

    val = int(x / y)
    print(val) # 5

    val = float(x)
    print(val) # 16.0

    # 複素数
    val = 3 + 5j
    print(val.conjugate()) # (3-5j)
    # 乗数
    val = pow(2, 3)
    print(val) # 8
    val = 2 ** 3
    print(val)

    # 数値はTrue
    print(isinstance(1, numbers.Number))
    print(isinstance('Text', numbers.Number))

    # 指数関数
    val = math.exp(2)
    print(val)
    # 対数関数

    # イミュータブルか確認する
    num = 100
    text = "aaaa"
    dic = {'key': 200}

    print("num id = ", id(num))
    print("text id = ", id(text))
    print("dic id = ", id(dic))

    text1 = "aaa"
    text2 = text1
    text3 = text1 + 'bbb'
    print("text1 id = ", id(text1))
    text1_id = id(text1)
    print("text2 id = ", id(text2))
    print("text3 id = ", id(text3))

    text1 = "bbb"
    print("text1 id = ", id(text1))
    text1_id_af = id(text1)

    if text1_id == text1_id_af:
        print("text1 id は同一です")
    else:
        print("text1 id は異なっています")

    x = 3
    y = 3
    z = 7

    b1 = (x == y)
    b2 = (x == z)

    print("b1 = ", b1)
    print("b2 = ", b2)

    x = [1, 2]
    y = x
    z = [1, 2]

    b1 = (x == y)
    b2 = (z == z)
    print("b1 = ", b1)
    print("b2 = ", b2)

    b3 = (x is y)
    b4 = (x is z)
    print("b3 = ", b3)
    print("b4 = ", b4)

    x = 3
    y = 5
    z = 7
    print("x < y = ", x < y)
    print("x < y < z = ", x < y < z)

    # for文
    datas = ['a', 'b', 'c']
    for v in datas:
        print("v = ", v)

    print("for in range")
    for v in range(1, 5, 2):
        print("v = ", v)

    print("for in dectionary")
    dic = {'key1': 110, "key2": 270, "key3": 570}
    for key in dic:
        print("dic[key] = ", dic[key])

    # dictionary型の値でループしたい場合、valuesメソッドを使用
    print("for in dectionary's values method")
    for value in dic.values():
        print("value = ", value)

    # dictionary型のkey,valueの両方を取得したい場合は、itemsメソッドを使用
    for key, value in dic.items():
        print("key = ", key, ", value = ", value)

    l = ['a', 'b', 'c']
    for i, value in enumerate(l):
        print("index = ", i, ", value = ", value)

    # dictionary型
    for i, (key, value) in enumerate(dic.items()):
        print(i, key, value)

    
    data_list = [1, 2, 3]

    for data in data_list:
        print("data = ", data)
        if data > 1:
            print("Break!!!")
            break
    
    data_list = []
    for data in data_list:
        print("data = ", data)
    else:
        print("ループ処理が終わりました")

    l = [0, 3, 1, 10]
    for x in l:
        if x < 0:
            print("負の数を検知しました")
            break
    else:
        print("負の数は見つかりませんでした")

    






    