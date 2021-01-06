n1 = 18
n2 = 42
i = 1
x = 0

while i < n2:

    if (n1 % i == 0 and n2 % i == 0):
        x = i

    i += 1

print('The Greatest Common Divisor of ', n1 ,"and", n2 , 'is: ', x)

