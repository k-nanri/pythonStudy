
class MyDescriptor:
    
    def __init__(self, text):
        self.text = text

    def __get__(self, instance, owner):
        return "* " + self.text
    
    def __set__(self, instance, text):
        self.text = text + "!"

    def __delete__(self, instance):
        del self.text
        print("text属性が削除されました")

class Sample:
    """　属性にディススクリプタを持つ """
    descriptor = MyDescriptor("sample")

if __name__ == '__main__':

    obj = Sample()
    print(obj.descriptor)

    obj.descriptor = 'sample2'
    print(obj.descriptor)

    del obj.descriptor
    print(obj.descriptor)
    
