# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Investment:
    
    def __init__(self, principal, interest):
        
        self._principal = principal
        self._interest = interest
    
    def value_after (self, i, n):
        
        n = int(input('Number of years\n'))
        
        
        self._value = i
        self._years = n
        
        
        i = self._principal*(1 + self._interest)^n
        
        return i
    
    def __str__(self):
        
        return "Principal - " + str(self._principal) + ", Interest Rate - " + str(self._interest) + "%"

        