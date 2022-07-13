class Investment:
    
    def __init__(self, principal, interest):
        self._principal = principal
        self._interest = interest/100

    def value_after(self, years):
        return self._principal * (1 + self._interest) ** years

    def getPrincipal(self):
        return self._principal

    def setPrincipal(self, principal):
        self._principal = principal

    def __str__(self):
        return "Principal - " + str(self._principal) + \
               "\nInterest - " + str(self._interest)

'''
This child class can be in a separate file.
Just make sure you put them both in the
same folder and import the parent class.
'''

class AccessibleInvestment(Investment):
    
    def __init__(self, principal, interest):
        super().__init__(principal, interest)

    def withdraw(self, amount):
        new_principal = super().getPrincipal() - amount
        super().setPrincipal(new_principal)


'''
Using the classes
'''
inv = AccessibleInvestment(10000, 6)
print(inv)
print(inv.value_after(20))
inv.withdraw(2000)
print(inv)
print(inv.value_after(20))

     
