
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

