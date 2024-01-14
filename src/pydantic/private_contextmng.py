from contextlib import contextmanager

@contextmanager
def sample_context_mng():
    print("Start sample_context_mng")
    try:
        print("Call yield")
        yield
    finally:
        print("Finally")

with sample_context_mng():
    print("Start!!")

print("End!!")
