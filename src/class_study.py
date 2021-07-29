
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

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

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



