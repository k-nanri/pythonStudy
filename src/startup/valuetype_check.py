
def sample(obj):

    """ 引数の型を判定する """
    if isinstance(obj, bool):
        print("bool型です")
    
    if isinstance(obj, int):
        print("int型です")

    if isinstance(obj, float):
        print("float型です")

    if isinstance(obj, complex):
        print("complex型です")

    if isinstance(obj, list):
        print("list型です")

    if isinstance(obj, tuple):
        print("tuple型です")
    
    if isinstance(obj, range):
        print("range型です")

    if isinstance(obj, str):
        print("str型です")

    if isinstance(obj, set):
        print("set型です")
    
    if isinstance(obj, frozenset):
        print("frozenset型です")

    if isinstance(obj, dict):
        print("dict型です")


if __name__ == '__main__':

    sample("aaa")
    sample(1)
    sample(1.1)
    sample([1, 2, 3])
    sample({100, 200})
    sample({'key': 100})

