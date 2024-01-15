from contextlib import contextmanager

@contextmanager
def sample_context_mng():
    print("Start sample_context_mng")
    try:
        print("Call yield")
        yield "hoge"
    finally:
        print("Finally")

with sample_context_mng() as aaa:
    print("Start!!")
    print("Value = " + str(aaa))

print("End!!")
