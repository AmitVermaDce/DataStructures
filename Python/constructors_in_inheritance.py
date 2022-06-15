class Father(object):

    def __init__(self):
        self.money = 1000
        print("Father class constructor called!")

    def show(self):
        print("Father class Instance method")


class Son(Father):
    def disp(self):
        print("Son class Instance method!")


obj = Son()  # It shows Father class init method is called
obj.show()
obj.disp()
