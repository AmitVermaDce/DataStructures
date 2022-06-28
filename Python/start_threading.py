''' Creating a thread without using class
To create our own thread we need to create an object of Thread class.
Following are the ways of creating threads:-
1. Creating a thread without using a class
2. Creating a thread by creating a child class to Thread class
3. Creating a thread without creating child class to Thread class
'''

from threading import Thread


def disp():
    print("Child Thread!!")


for i in range(5):
    obj = Thread(target=disp)
    obj.start()

for i in range(5):
    print("Main Thread!")
