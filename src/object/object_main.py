
class Sample:

    def __init__(self):
        print("__init__")

    def call(self):
        print("call")


if __name__ == '__main__':

    # パラメータなし
    sample = Sample()
    sample.call()
