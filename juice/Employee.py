class Employee:
    """
    class variables
    demo in classVariablesDemo.py
    """
    raise_rate = 1.04
    num_of_employees = 0


    def __init__(self, fname, sname, pay):
        self.fname = fname
        self.sname = sname
        self.email = fname + sname + '@inc.com'
        self.pay = pay

        Employee.num_of_employees += 1  # constant across all class instances

    def fullname(self):
        return '{} {}'.format(self.fname, self.sname)

    def give_raise(self):
        self.pay = int(self.pay * self.raise_rate)

    '''
    class methods Demo in: classmethodsDemo.py
    '''

    @classmethod
    def set_raise_rate(cls, amount):
        cls.raise_rate = amount

    '''
    Usage of a class as alternative Constructor
    demo: classmethods2Demo.py 
    '''

    @classmethod
    def from_string(cls, employee_str):
        fname, sname, pay = employee_str.split('-')

        return cls(fname, sname, pay)

    '''
    Usage of static methods
    demo: staticmethodsDemo.py
    '''
    @staticmethod
    def is_workingday(day):
        if day.weekday() > 4:
            return False
        return True

    '''
    Dunder Methods
    '''
    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.fname,self.sname,self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay