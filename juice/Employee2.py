class Employee2:

    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname

    @property
    def email(self):
        return '{}{}@inc.com'.format(self.fname, self.sname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.sname)

    @fullname.setter
    def fullname(self, name):
        first, second = name.split(' ')
        self.fname = first
        self.sname = second

    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.sname = None
        print('Deleted name\n')
