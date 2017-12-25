class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first="Alex"
emp_1.last ="Kagai"
emp_1.email ="alexkagai@inc.com"
emp_1.pay =50000

emp_2.first="Alex2"
emp_2.last ="Kagai2"
emp_2.email ="alexkagai2@inc.com"
emp_2.pay =60000

print(emp_1.email)
print(emp_2.email)