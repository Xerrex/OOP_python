#! /usr/bin/python
from .Employee import Employee

class Developer(Employee):
    raise_rate = 1.10 # overrides parent : developerDemo.py

    def __init__(self, fname, sname, pay, prog_lang):
        super().__init__(fname, sname, pay)
        self.prog_lang = prog_lang

