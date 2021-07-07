import sys

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



    