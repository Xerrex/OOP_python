class Employee:
    def __init__(self,fname,sname,pay):
        self.fname = fname
        self.sname = sname
        self.email = fname + sname +'@inc.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.sname)


emp_1 = Employee('Alex', 'Kagai', 50000)
emp_2 = Employee('Alex2', 'Kagai2', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.fullname()) #print(Employee.fullname(emp_1))

print(emp_1.email)

print("\n###################################\n")
print(emp_2.fullname()) #print(Employee.fullname(emp_2))
print(emp_2.email)
