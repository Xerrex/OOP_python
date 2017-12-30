#! /usr/bin/python
from .Employee import Employee


class Manager(Employee):

    def __init__(self, fname, sname, pay, employees=None):
        super().__init__(fname, sname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_Employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def list_employees(self):
        for employee in self.employees:
            print('-->', employee.fullname())
