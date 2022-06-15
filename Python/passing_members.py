# Passing members of One Class to Another Class

class Student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    def disp(self):
        print("<--Inside Student Class-->")
        print("Student Name:", self.name)
        print("Student Roll No:", self.roll)


class User:

    @staticmethod
    def show(obj):
        print("<--Inside User class-->")
        print("Username:", obj.name)
        print("User Roll No:", obj.roll)
        print()
        obj.disp()


obj = Student("Amit Verma", 24)
# Object of one class pass to another class --> Now all members of one class is visible to another class
User.show(obj)
