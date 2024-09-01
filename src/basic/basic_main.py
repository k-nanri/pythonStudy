class Sample():
    pass

class HeadSample(Sample):
    pass

def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


def sample1():
    try:
        try:
            f()
        except* OSError as e:
            print("There were OSErrors")
            raise Exception("OSErrosだよ")
        except* SystemError as e:
            print("There were SystemErrors")
            raise Exception("SystemErrorsだよ")
    except Exception as e:
        print(f"raiseされたよ {type(e)}")


def sample2():

    try:
        raise TypeError("bad type")
    except Exception as e:
        e.add_note("Add some information")
        e.add_note("Add saome more information")
        raise


def multi(x):
    y = x*2
    return y


def gettwo(x):
    if x % 2 == 0:
        return x
    else:
        return None


def sort2(x):
    print(x)
    if x == 4:
        return True
    else:
        return False

def builtin():

    print(f"abs func = {abs(+3.5)}")

    all_sample = []
    print(f"all func = {all(all_sample)}")

    all_sample2 = []
    print(f"all_sample2 = {any(all_sample2)}")

    # ascii
    print(f"ascii = {ascii("あああああ")}")
    print(f"ascii = {ascii("aaa")}")

    # bin
    print(f"bin = {bin(8)}")

    # callable
    print(f"not function = {callable("aaaa")}")
    print(f"function     = {callable(sample1)}")

    # dir
    print(f"dir = {dir()}")

    # enumrate
    arry = ["aaaa", "bbbb", "cccc", "dddd"]
    for i, d in enumerate(arry):
        print(f"i = {i}, d = {d}")
        
    print(filter(lambda i: i == "aaaa", arry))

    # fronzenset
    aaa = frozenset({"aaa", "ccc"})
    print(aaa)
    
    # globals
    print(globals())

    # hash
    a = "test12345"
    b = "test12345"
    print(f"a hash = {hash(a)}")
    print(f"b hash = {hash(b)}")

    # hex
    print(f"hex = {hex(25)}")

    # id
    print(f"id  = {id(a)}")

    # input
    s = input("入力してください:")
    print(f"input result = {s}")

    # insinsttance
    s1 = Sample()
    s2 = HeadSample()

    print(f"Is s1 Sample ?     : {isinstance(s1, Sample)}")
    print(f"Is s1 HeadSample ? : {isinstance(s1, HeadSample)}")
    print(f"Is s2 Sample ?     : {isinstance(s2, Sample)}")
    print(f"Is s2 HeadSample ? : {isinstance(s2, HeadSample)}")

    i1 = list()
    i1.append("aaa")
    i1.append("bbb")
    i1.append("ccc")
    i1.append("ddd")
    i1.append("eee")

    print(f"Type = {type(i1)}")
    print(f"Type = {type(iter(i1))}")

    # map
    for i in i1:
        print(i)

    num = [1, 2, 3, 4, 5]
    print(f"num * 2 = {list(map(multi, num))}")

    # filter
    print(f"filter = {list(filter(gettwo, num))}")

    # max
    print(f"max = {max(num)}")
    
    try:
        max([])
    except ValueError:
        print("raise ValueError.")

    print(f"max default = {max([], default=10)}")
    print(f"max = {max(num, key=sort2)}")

    # next
    print(f"next = {next(iter(num))}")
    
    # tuple
    a = ("a", "b", "c")
    for aa in a:
        print(aa)

    for item in zip([1, 2, 3], ["aaa", "bbb", "ccc", "ddd"]):
        print(item)


def list_and_tuple_and_set():

    print("========================================")
    print(" list and tuplle and set")
    print("========================================")

    a = {1, 1, 2, 2, 3, 3}
    print(a)

    bb = {}
    bb["1"] = "aa"
    bb["3"] = "bb"
    bb["2"] = "cc"
    print(bb)

    a1 = [1, 1, 2, 2, 3, 3,]
    print(f"a1 = {a1}")
    a2 = set(a1)
    print(f"a2 = {a2}")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x





# sample1()
# sample2()
builtin()
list_and_tuple_and_set()
x = lambda a, b: a + b + 10
print(x(5, 5))

myclass = MyNumbers()
myiter = iter(myclass)
print("== iterator =====")
print(next(myiter))
print(next(myiter))
