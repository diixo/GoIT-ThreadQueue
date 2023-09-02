# https://gist.github.com/arthuralvim/356795612606326f08d99c6cd375f796
# https://superfastpython.com/thread-queue-task-done-join/
# https://stackoverflow.com/questions/27200674/python-queue-join

from queue import Queue
from threading import Thread

num_worker_threads = 1
q = Queue()

def do_work(item):
    print(item)

def source():
    return range(50)

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


threads = []

for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.start()
    threads.append(t)


for item in source():
    q.put(item)

# block until all tasks are done
q.join()

print('stopping workers!')

# stop workers
for i in range(num_worker_threads):
    q.put(None)

for t in threads:
    t.join()