from Employee import Employee

'''
Demo file shows usage of class methods
as alternative constructor
'''

emp_str_1 = "Jone-Kotas-100000"
emp_str_2 = "William-Helimson-500000"
emp_str_3 = "Meli-YaMchicha-60000"

emp_1 = Employee.from_string(emp_str_1)
emp_2 = Employee.from_string(emp_str_2)
emp_3 = Employee.from_string(emp_str_3)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)