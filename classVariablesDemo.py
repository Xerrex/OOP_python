from Employee import Employee

emp_1 = Employee('Alex', 'Kagai', 50000)
emp_2 = Employee('Alex2', 'Kagai2', 60000)


print("\n#Pay raise#")
print(emp_1.pay)
emp_1.give_raise()
print("new pay after raise is: " + str(emp_1.pay))

#getting the namespace: Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

#getting the Number of Employees
print("\nNumber of employees: ", Employee.num_of_employees)
