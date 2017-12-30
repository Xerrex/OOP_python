#! /usr/bin/python
from juice.Employee import Employee

class Developer(Employee):
    pass



dev1 = Developer('AlexDev', 'Kagai', 50000)
dev2 = Developer('Alex2Dev', 'Kagai2', 60000)

print(dev1.email)
print(dev2.email)

#print(help(Developer)) uncomment to info about Developer class

print("\n\nraise rate:",dev1.raise_rate)
print('\ndev1 pay:',dev1.pay)

dev1.give_raise()
print('dev1 pay after raise:',dev1.pay)