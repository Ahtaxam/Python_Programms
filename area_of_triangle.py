# This programm will calculate the area of traingle

import math as m

print("Enter the value of side A of triangle: " ,end=' ')
a = int(input())

print("Enter the value of side B of triangle: " ,end=' ')
b = int(input())

print("Enter the value of side C of triangle: " ,end=' ')
c = int(input())


# first find s

s = (a + b + c) // 2

area = s * (s-a) * (s-b) * (s-c)

area = m.sqrt(area)

print('Area of triangle is:' ,area)
