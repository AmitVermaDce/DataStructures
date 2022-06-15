import threading
from threading import Thread
import time


def thredFunc():
    print("Starting a Thread function")
    time.sleep(5)
    print("Thread Function Completed")

thredFunc()
print(threading.activeCount())

