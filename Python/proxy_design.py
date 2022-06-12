from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        print("Interface Method")


class Person(IPerson):

    def person_method(self):
        print("I am a Person!")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy method!!!!")
        self.person.person_method()

p1 = ProxyPerson()
p1.person_method()
