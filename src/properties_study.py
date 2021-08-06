class Sample:

    def __init__(self):
        self.__text = "sample"

    @property
    def text(self):
        return "({0})".format(self.__text)

    @text.setter
    def text(self, text):
        if text is None:
            self.__text = "None"
        else:
            self.__text = text

    @text.deleter
    def text(self):
        pass

if __name__ == '__main__':

    obj = Sample()
    print(obj.text)

    obj.text = None
    print(obj.text)

    del obj.text
    print(obj.text)

