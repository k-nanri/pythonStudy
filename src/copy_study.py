import copy

class Sample():

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text

    def __deepcopy__(self, memo):
        new_obj = Sample(self.text)
        return new_obj

if __name__ == '__main__':

    data1 = {'key1':100, 'key2':[1, 2]}
    data2 = copy.copy(data1)

    del data2['key1']
    print("=== copy.copy ============")
    print("data1 = ", data1)
    print("data2 = ", data2)
    
    # 内部で保持しているオブジェクトの参照は同じのため、影響がでている
    data2['key2'][0] = 999
    print("data1 = ", data1)
    print("data2 = ", data2)

    print("=== copy.deepcopy ============")
    data1 = {'key1':100, 'key2':[1, 2]}
    data2 = copy.deepcopy(data1)

    data2['key2'][0] = 999
    print("data1 = ", data1)
    print("data2 = ", data2)

    # 独自クラスの場合は__deepcopy__という特殊メソッドの実装が必要
    data1 = {'key1':100, 'key2':Sample('obj')}
    data2 = copy.deepcopy(data1)

    data2['key2'].text = 'hoge'
    print("data1 = ", data1)
    print("data2 = ", data2)