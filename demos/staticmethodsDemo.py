#! /usr/bin/python
from juice.Employee import Employee
import datetime

myday = datetime.date(2017,12,31)

print(myday)
print(Employee.is_workingday(myday))

