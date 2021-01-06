#This programm demonstrae one of math problem called piece wise function
import math as m 

print("Enter X: ",end=' ')
x = int(input())

if x == 2:
    print(6)

elif x < 2:
    print(m.sqrt(x))

elif (x > 2) and (x <= 6):
    print(10 - x)

elif x > 6:
    x = (m.sqrt(x) + 7)
    print(x,0.5)