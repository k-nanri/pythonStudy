import threading
import queue

q = queue.Queue(maxsize=0)

def worker():

    while True:
        item = q.get()
        print(f'Working on ${item}')
        print(f'Finished {item}')
        q.task_done()

if __name__ == '__main__':

    threading.Thread(target=worker, daemon=True).start()

    for item in range(30):
        q.put(item)

    print("All task requests send\n", end="")
    q.join()
    print("All work completed")

