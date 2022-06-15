class Father(object):
    def __init__(self):
        print("Father class constructor")

    def showF(self):
        print("Father class instance method")


class Son(Father):
    def __init__(self):
        super(Son, self).__init__()
        print("Son class constructor")

    def showS(self):
        print("Son class instance method")


class Daughter(Father):
    def __init__(self):
        super(Daughter, self).__init__()
        print("Daughter class constructor")

    def showD(self):
        print("Daughter class 2 instance method")


obj = Son()
print()
obj1 = Daughter()
