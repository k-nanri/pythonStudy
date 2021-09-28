import threading
import time

def execute_thread1():

    print("thread1 start")
    time.sleep(10)
    print("thread1 end")

def execute_thread2():

    print("thread2 start")
    time.sleep(5)
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