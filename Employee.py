class Employee:
    '''
    class variables
    demo in classVariablesDemo.py
    '''
    raise_rate = 1.04
    num_of_employees = 0

    def __init__(self,fname,sname,pay):
        self.fname = fname
        self.sname = sname
        self.email = fname + sname +'@inc.com'
        self.pay = pay

        Employee.num_of_employees+=1 # constant across all class instances

    def fullname(self):
        return '{} {}'.format(self.fname, self.sname)

    def give_raise(self):
        self.pay = int(self.pay * self.raise_rate)
