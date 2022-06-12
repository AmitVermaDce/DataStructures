class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last



p1 = Employee("Amit", "Verma")
p1.fullname = "Amit Vermaaaaaa"
print(p1.email)
p2 = Employee("Corey", "Schafer")
print(p1.__dict__)
print((p2.__dict__))
