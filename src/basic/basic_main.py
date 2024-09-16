from pathlib import Path
import asyncio
import time

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


class MyData:
    def __init__(self, x: int):
        self.x = x


class MyDataMng:

    def __init__(self):
        self.data: list[MyData] = []
        self.max = len(self.data)

    def add(self, mydata: MyData):
        self.data.append(mydata)
        self.max = len(self.data)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            data = self.data[self.n]
            self.n += 1
            return data
        else:
            raise StopIteration


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

mydatamng = MyDataMng()
mydatamng.add(MyData(1))
mydatamng.add(MyData(2))
mydatamng.add(MyData(3))

print("== 自作iterator ===")
for d in mydatamng:
    print(d.x)

print("== Pathlib =========")
p = Path("../")
for x in p.iterdir():
    if x.is_dir():
        print(x)


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():

    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


print("Async!!")
asyncio.run(main())


async def main2():
    async with asyncio.TaskGroup() as tg:
        task11 = tg.create_task(
            say_after(1, "hello2")
        )
        task22 = tg.create_task(
            say_after(2, "world2")
        )
        print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")


print("TaskGroup!!")
asyncio.run(main2())


async def test_gather(sleep_time, value):
    await asyncio.sleep(sleep_time)
    return value


print("gather start")
async def main3():
    results = await asyncio.gather(
                test_gather(1, "aaa"),
                test_gather(2, "bbb"),
                test_gather(5, "ccc")
            )
    for r in results:
        print(f"result = {r}")

asyncio.run(main3())


async def long_task():
    print(f"Start Sleep {time.strftime('%X')}")
    await asyncio.sleep(30)
    print(f"Wake Up!! {time.strftime('%X')}")


async def main4():
    print(f"Timeout Sample is started {time.strftime('%X')}")
    try:
        async with asyncio.timeout(10):
            await long_task()
    except TimeoutError:
        print("Timeout!!")

    print(f"Timeout Sample is Finished {time.strftime('%X')}")

asyncio.run(main4())

async def main5():
    print(f"Timeout sample2 started {time.strftime('%X')}")
    try:
        async with asyncio.timeout(None) as cm:
            new_timeout = 30
            cm.reschedule(new_timeout)

            await long_task()

    except TimeoutError:
        print("Timeout2!!")
    
    print("cm.expired = " + str(cm.expired()))
    if cm.expired():
        print("Looks")

    print(f"Timeout Sample2 is Finished!!! {time.strftime('%X')}")

asyncio.run(main5())


async def main6():
    print(f"Timeout Sample3 is started {time.strftime('%X')}")
    try:
        async with asyncio.timeout_at(100):
            await long_task()
    except TimeoutError:
        print("Timeout!!")

    print(f"Timeout Sample3 is Finished {time.strftime('%X')}")

asyncio.run(main6())

async def main6():
    print(f"Timeout Sample4 is started {time.strftime('%X')}")
    try:
        await asyncio.wait_for(long_task(), 10)
    except TimeoutError:
        print("Timeout!!")

    print(f"Timeout Sample4 is Finished {time.strftime('%X')}")

asyncio.run(main6())

# リストの内包表記

name = [0 for i in range(10)]
print(f"name = {name}")

name = [i ** 2 for i in range(10)]
print(f"name = {name}")

name = [0 if i % 2 == 0 else 1 for i in range(10)]
print(f"name = {name}")

s = 'Bye'
l = [' ' + char.upper() + ' ' for char in s]
print(f"l = {l}")

s1 = []
for i in range(20):
    s1.append(i)

print(f"s1 = {s1}")

s2 = [i for i in s1 if i % 2 == 0]
print(f"s2 = {s2}")

print("--- ネストしたループ ------")
for var1 in range(3):
    for var2 in range(2):
        print((var1, var2))


print("--- リスト内包表記 -------")
l2 = [(var1, var2) for var1 in range(3) for var2 in range(2)]
print(l2)

print("--- ジェネレータ式 -------")


def squares(length):
    for n in range(length):
        yield n ** 2


for square in squares(5):
    print(square)

l3 = (n ** 2 for n in range(10))
for ll in l3:
    print(ll)
