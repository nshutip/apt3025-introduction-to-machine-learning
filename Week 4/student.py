# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:03:15 2022

@author: LENOVO
"""

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def setAge(self, age):
        self._age = age
        
    def __str__(self):
        return "Name: " + self._name + \
            "\nAge: " + str(self._age)
            
    