from abc import ABC, abstractmethod


class Father(ABC):

    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete method...")


class Child(Father):

    def disp(self):
        print("Child Class!")
        print("Defining Abstract method...")

obj = Child()
obj.disp()
obj.show()
