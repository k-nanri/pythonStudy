import sys

print("Hello World")


if __name__ == '__main__':

    args = sys.argv

    if len(args) == 3:
    
        # スクリプト名
        print(args[0])
        # 1番目の引数
        print(args[1])
        print(args[2])

    else:
        print('以下の形式でパラメータを指定すること')
        print('$ study.py aaa bbb')
        quit()