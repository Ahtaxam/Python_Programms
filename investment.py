
import math

class Investment:
    def __init__(self,principal,interest_rate):
        self.principal = principal
        self.interest_rate = interest_rate

    def value_after(self , n):
        x = self.principal * (1 + self.interest_rate)
        return math.pow(x,n)



x = Investment(100000 , 5.12)
print("The intrest would be: " ,x.value_after(5))


