class Father(object):
    def __init__(self):
        print("Father class constructor")

    def showF(self):
        print("Father class instance method")


class Child(Father):
    def __init__(self):
        super(Child, self).__init__()
        print("Child class constructor")

    def showC(self):
        print("Child class instance method")


class GrandChild(Child):
    def __init__(self):
        super(GrandChild, self).__init__()
        print("Grand Son class constructor")

    def showG(self):
        print("GrandChild class instance method")


obj = GrandChild()
