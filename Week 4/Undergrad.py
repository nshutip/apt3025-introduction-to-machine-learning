# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:09:55 2022

@author: LENOVO
"""

from student import Student

class Undergrad(Student):
    def __init__(self, name, age, major):
        Student.__init__(self, name, age)
        self._major = major
        
    def __str__(self):
        return Student.__str__(self) + '\n' + \
            'major' + self._major