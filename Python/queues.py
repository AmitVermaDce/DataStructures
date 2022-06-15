'''
The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded
programming when information must be exchanged safely between multiple threads.

'''
import queue

q = queue.Queue()

for val in range(5):
    q.put(val)
while not q.empty():
    print(q.get())
