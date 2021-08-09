
if __name__ == '__main__':

    text1 = "aaa"
    text2 = "bbb"
    text3 = "ccc"

    text = text1 + text2 + text3
    print("text = ", text)

    label = "pi = "
    val = 3.14
    text = label + str(val)
    print(text)

    # join
    data = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    csv = ','.join(data)
    print("csv = ", csv)

    # split
    data = "aaa bbb ccc ddd eee"
    data_list = data.split(' ')
    print("data_list = ", data_list)

    # replace
    text = 'xxxbbbcc'
    new_text = text.replace('x', 'a')
    print("before = ", text)
    print("after  = ", new_text)

    text = 'abcdefghigklmn'

    print("text[0]   = ", text[0])
    print("text[3]   = ", text[3])
    print("text[-1]  = ", text[-1])
    print("text[0:3] = ", text[0:3])

    # 文字列が含まれているかどうか判定する
    print('cde' in text)

    # 1文字ずつ処理
    for s in text:
        print("s = ", s)

    text = 'abcabc'
    print(text.find('bc'))
    print(text.rfind('bc'))

    # トリミング
    text = ' abcabc '
    print(text.strip())
    print(text.lstrip())
    print(text.rstrip())

    text = 'abcDEFG'
    print(text.upper())
    print(text.lower())
    print(text.capitalize())
    
