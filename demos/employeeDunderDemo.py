from juice.Employee import Employee

emp_1 = Employee('Alex', 'Kagai', 50000)
emp_2 = Employee('Alex2', 'Kagai2', 60000)

print("Usage of __repr__")
print(emp_2.__repr__())

print("\nUsage of __str__")
print(emp_2)
print(emp_2.__str__())

print("\nAdding to Employee objects")
print(emp_1 + emp_2)