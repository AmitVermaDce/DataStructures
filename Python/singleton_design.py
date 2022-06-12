from abc import ABCMeta, abstractstaticmethod


class IPerson:

    @abstractstaticmethod
    def print_data():
        print("Implemented in Child Case")


class PersonSingleton(IPerson):
    __instance = None

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance == self

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default instance", 23)
        return PersonSingleton.__instance

    @staticmethod
    def get_data():
        print(f"Name: {PersonSingleton.__instance.name} and Age: {PersonSingleton.__instance.age}")

p1 = PersonSingleton("Amit", 30)
p1.print_data()
