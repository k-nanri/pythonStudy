import backoff
import time

count = 1

def fatal_code(e):
    return False

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


@backoff.on_predicate(backoff.constant, jitter=None, interval=1)
def polling():
    print("Start Polling")
    time.sleep(3)
    return False

if __name__ == '__main__':
    polling()
    handle()