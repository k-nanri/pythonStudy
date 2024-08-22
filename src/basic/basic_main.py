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


def builtin():

    print(f"abs func = {abs(+3.5)}")

    all_sample = []
    print(f"all func = {all(all_sample)}")

    all_sample2 = []
    print(f"all_sample2 = {any(all_sample2)}")


# sample1()
# sample2()
builtin()
