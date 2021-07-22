
if __name__ == '__main__':

    dic = {'key1': 110, 'key2':270, 'key3': 350}
    print("dic = ", dic)

    # キー指定でのアクセス
    print(dic['key1'])

    try:
        print("dic[hoge] = ", dic['hoge'])
    except Exception as e:
        print("Not Found Key")
        print(e)

    # dictionaryオブジェクトのgetメソッドを使用
    print("dic.get(key1) = ", dic.get('key1'))
    print("dic.get(hoge) = ", dic.get('hoge'))

    # 値の更新
    dic['key1'] = 500
    print("dic[key1] = ", dic['key1'])

    # オブジェクト生成して値を設定
    dic = dict()
    print("dic = ", dic)
    dic['key1'] = 110
    dic['key2'] = 270
    dic['key3'] = 350

    str = 'key4'
    dic[str] = 500
    print("dic = ", dic)

    # dictionaryの要素数
    print(len(dic))

    for item in dic:
        print("key = ",item, ", value = ", dic[item])

    




    