import time
import threading
from concurrent.futures import ThreadPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)

def task(v):

    getLogger().info("%s start", v)
    time.sleep(1.0)
    getLogger().info("%s end", v)

def execute_thread1():

    print("thread1 start")
    time.sleep(5)
    print("thread1 end")

def execute_thread2():

    print("thread2 start")
    time.sleep(3)
    print("thread2 end")

if __name__ == '__main__':

    print(threading.active_count())
    print(threading.current_thread())

    thread1 = threading.Thread(target=execute_thread1)
    thread2 = threading.Thread(target=execute_thread2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("main end")

    # ThreadPoolExecutorの実装
    # Python3.2 から追加されたconcurrent.cuturesモジュールを使用する
    init_logger()
    getLogger().info("main start")
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
        
        for i in range(5):
            executor.submit(task, i)
            getLogger().info("submit end")
            getLogger().info("main end")



