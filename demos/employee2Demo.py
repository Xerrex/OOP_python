from juice.Employee2 import Employee2

emp_1 = Employee2('Alex', 'Kagai')
print(emp_1.fname)
print(emp_1.email, '\n')

emp_1.fname = 'Xela'
print(emp_1.fname)
print(emp_1.email)


emp_1.fullname = 'Brian Medea'
print('\n', emp_1.fname)
print(emp_1.email, '\n')

del emp_1.fullname

print(emp_1.fullname)