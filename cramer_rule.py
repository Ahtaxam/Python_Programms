# In this program we will find value of two variable through crammer Rule

print("Enter value of a1: " ,end=' ')
a1 = int(input())

print("Enter value of b1: " ,end=' ')
b1 = int(input())

print("Enter value of c1: " ,end=' ')
c1 = int(input())

print("Enter value of a2: " ,end=' ')
a2 = int(input())

print("Enter value of a2: " ,end=' ')
b2 = int(input())

print("Enter value of a2: " ,end=' ')
c2 = int(input())

# first calculate determinent of Given equation
D = (a1 * b2) - (a2 * b1)

# now calculate DX
DX = (c1 * b2) - (c2 * b1)

# now calculate DY
DY = (a1 * c2) - (a2 * c1)

# calculate X
X = DX // D

# calculate Y
Y = DY // D



print("X = ",X )
print("Y = ",Y)