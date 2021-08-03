
class Sample():
    
    def __init__(self):

        self.a = 0
        self._b = 0
        self.__c = 0
        self.__d_ = 0
        self.__e__ = 0

if __name__ == '__main__':

    obj = Sample()
    a = obj.a
    b = obj._b

    # AttributeErrorを発生
    try:
        c = obj.__c
    except AttributeError as e:
        print(e)

    try:
        d = obj.__d_
    except AttributeError as e:
        print(e)

    e = obj.__e__
    
