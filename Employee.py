class Employee:
    '''
    class variables
    '''
    raise_rate = 1.04
    num_of_emps = 0

    def __init__(self,fname,sname,pay):
        self.fname = fname
        self.sname = sname
        self.email = fname + sname +'@inc.com'
        self.pay = pay

        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.fname, self.sname)

    def give_raise(self):
        self.pay = int(self.pay * self.raise_rate)


emp_1 = Employee('Alex', 'Kagai', 50000)
emp_2 = Employee('Alex2', 'Kagai2', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.fullname()) #print(Employee.fullname(emp_1))
print(emp_1.email)

print("\n###################################\n")
print(emp_2.fullname()) #print(Employee.fullname(emp_2))
print(emp_2.email)

print("\n#Pay raise#")
print(emp_1.pay)
emp_1.give_raise()
print("new pay after raise is: " + str(emp_1.pay))

#getting the namespace: Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

#getting the Number of Employees
print("\nNumber of employees: ", Employee.num_of_emps)
