class Father(object):
    money = 1000

    def show(self):
        print("Parent Class instance method!")

    @classmethod
    def showmoney(cls):
        print("Parent class Class method:", cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class stat method:", a)


class Son(Father):
    def disp(self):
        print("Child class Instance method!")


obj = Son()
obj.disp()  # Child class Instance method
obj.show()  # Parent class Instance method
obj.showmoney()  # Parent class Class method
obj.stat()  # Parent class static method
