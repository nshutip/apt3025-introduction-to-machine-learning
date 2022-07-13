# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:10:52 2022

@author: LENOVO
"""

from investment import Investment

class AccessibleInvestment(Investment):
    
    def __init__(self, principal, interest):
        Investment.__init__(self, principal, interest)
        self._principal = principal
        self._interest = principal

    def withdrawal(self, amount):
        
        self._amount = amount
        
        if amount > self._principal:
            return "The Amount To be withdrawn is greater than the balance"
        
        else:
            return "You have Withdrawn " + str(amount) + ". Available Balance: " + str(self._principal-amount)
    
    