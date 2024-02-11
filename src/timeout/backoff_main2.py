import backoff
import time

def fatal_code(e):
    return True

@backoff.on_exception(backoff.constant,
                      Exception,
                      raise_on_giveup=True,
                      giveup=fatal_code,
                      jitter=None,
                      interval=[1, 10, 15]
                      )
def handle():
    print("Start handle")
    time.sleep(2)
    raise Exception()
    print("End handler")


if __name__ == '__main__':
    handle()