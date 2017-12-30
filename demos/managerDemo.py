#! /usr/bin/python
from juice.Manager import Manager
from juice.Developer import Developer

dev1 = Developer('AlexDev', 'Kagai', 50000,'python')

dev2 = Developer('Alex2Dev', 'Kagai2', 60000,'javascript')

dev3 = Developer('Igor','Lukalvich',100000,'C++')


manager_1 = Manager('Jone', 'Kotas', 100000,[dev1,dev3])

print(manager_1.email)
print('\n', manager_1.list_employees())

manager_1.add_Employee(dev2)
print('\n',manager_1.list_employees())

manager_1.remove_employee(dev1)
print('\nlist of employees after removing dev1')
print(manager_1.list_employees())



