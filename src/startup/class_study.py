import math

class Base1:
    def func1(self):
        print("func1")

class Base2:
    def func2(self):
        print("func2")

class Sub2(Base1, Base2):
    def func(self):
        super().func1()
        super().func2()

class Base:
    def func1(self):
        print('funct1')

    def over(self):
        print("over function")

class Sub(Base):
    def func2(self):
        super().func1()
        print('func2')

    def over(self):
        print("Sub over function")

class MyClass():
    remark = "A"

    def __init_(self):
        self.text = "sample text"

class Sample:

    def __init__(self):
        self.x = 100


class Coordinate:
    """座標クラス"""

    def __init__(self):
        # 初期化
        self.x = 0
        self.y = 0

    def move(self, x, y):
        # 平行移動
        self.x += x
        self.y += y

    def show_coordinate(self):
        print(self.x, self.y)

    @classmethod
    def create_new_cood(cls, x, y):
        # オブジェクトを生成して返す
        new_cood = cls()
        new_cood.x = x
        new_cood.y = y
        return new_cood

    @staticmethod
    def calc_dist(cood1, cood2):
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


class MyClass2:
    def __new__(cls):
        print('__new__')
        print("cls = ", cls)

    def __init__(self):
        print('__init__')

    def __str__(self):
        return 'test'

if __name__ == '__main__':

    cood = Coordinate()
    cood.x = 100
    cood.y = 200
    cood.show_coordinate()

    print(cood)

    # 外部からのメンバ追加
    obj = Sample()
    obj.y = 200
    print("obj.y = ", obj.y)

    del obj.x
    try:
        print(obj.x)
    except AttributeError as e:
        print(e)

    # クラスをオブジェクトとして扱う
    C = Coordinate
    cood2 = C()
    cood2.x = 300
    cood2.y = 600
    cood2.show_coordinate()

    c1 = MyClass()
    c2 = MyClass()

    # クラス変数にアクセス
    print("c1.remark = ", c1.remark, "c2.remark = ", c2.remark, "MyClass.remark = ", MyClass.remark)

    # クラス変数を変更する
    MyClass.remark = "B"
    print("c1.remark = ", c1.remark, "c2.remark = ", c2.remark, "MyClass.remark = ", MyClass.remark)

    cood = Coordinate()
    cood2 = cood.create_new_cood(10, 20)
    cood2.show_coordinate()

    cood1 = Coordinate()
    cood1.x, cood1.y = 100, 100

    cood2 = Coordinate()
    cood2.x, cood2.y = 200, 200

    dist = Coordinate.calc_dist(cood1, cood2)
    print("dist = ", dist)

    obj = Sub()
    #obj.func1()
    obj.func2()
    obj.over()
    
    obj = Sub2()
    obj.func()

    # インスタンスアロケータの確認
    obj = MyClass2()

    

