from Employee import Employee

'''
 Demonstrates usages of class methods
'''

emp_1 = Employee('Alex', 'Kagai', 50000)
emp_2 = Employee('kaliente', 'Hapas', 60000)

#raise rate before increase
print('The Raise amounts before Increase')
print(Employee.raise_rate)
print(emp_1.raise_rate)
print(emp_2.raise_rate)

#raise amounts Now
Employee.set_raise_rate(1.05)

print('\n\n\nThe Raise amounts after Increase')
print(Employee.raise_rate)
print(emp_1.raise_rate)
print(emp_2.raise_rate)

