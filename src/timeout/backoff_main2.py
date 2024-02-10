import backoff
import time

@backoff.on_exception(backoff.runtime,
                      Exception,
                      jitter=None,
                      max_time=60)
def handle():
    print("Start handle")
    time.sleep(2)
    raise Exception()
    print("End handler")


if __name__ == '__main__':
    handle()