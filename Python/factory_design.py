from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        print("Interface Method!")


class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher"

    def person_method(self):
        print("I am a Teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()
        print("Invalid Type!!!!!!")
        return "Not a choice"

while True:
    obj = PersonFactory.build_person(input("Enter: "))
    obj.person_method()

