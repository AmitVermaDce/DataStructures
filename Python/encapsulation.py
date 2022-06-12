class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

p1 = Person("Amit", 23, "M")
p1.Name = "Amit Verma"
print(p1.Name)