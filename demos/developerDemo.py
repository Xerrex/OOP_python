#! /usr/bin/python
from juice.Developer import Developer
'''
Demonstrates overriding of the raise amount
'''

dev1 = Developer('AlexDev', 'Kagai', 50000)
dev2 = Developer('Alex2Dev', 'Kagai2', 60000)

print("\n\nraise rate:",dev1.raise_rate)
print('\ndev1 pay:',dev1.pay)

dev1.give_raise()
print('dev1 pay after raise:',dev1.pay)