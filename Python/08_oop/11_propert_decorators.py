class safe_locker:
    def __init__(self, money):
        self._money = money

    @property  #@property decorator turns a method into an attribute. also called getter
    def money(self):
        return self._money + 2
        
    @money.setter  #runs whenever you try to change the value, kind of gatekeeper
    def money(self, money):
        if 1 <= money <= 5:
            self._money = money
        else:
            raise ValueError("The security guard wont allow to add more money except the range 1 to 5")
            
rupees = safe_locker(2)
print(rupees.money)
# rupees.money = 6
# print(rupees.money)