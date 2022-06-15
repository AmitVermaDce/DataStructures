from abc import ABC, abstractmethod


class IFather(ABC):

    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass


class Child(IFather):

    def disp1(self):
        print("Child Class!")


class GrandChild(Child):

    def disp2(self):
        print("Grand Child class")


obj = GrandChild()
obj.disp2()
