from abc import ABC, ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employee):
        print("Implement in Child claass")

    @abstractstaticmethod
    def p_department():
        print("Implement in child class")


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def accounting(self):
        print(f"Accounting Department: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def accounting(self):
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_departemnt(self):
        print("Parent Department")
        print(f"Parent Department Base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total Number of employees: {self.employees}")


dept1 = Accounting(200)
dept2 = Development(100)
parentalDepartment = ParentDepartment(30)
parentalDepartment.add(dept1)
parentalDepartment.add(dept2)
parentalDepartment.print_departemnt()
