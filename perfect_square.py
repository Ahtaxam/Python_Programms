# it will compute sum of numbers
import math

print("Enter the n: ",end='')
n = int(input())
i = n
count = 0
count_1 = 0

while n > 0:

    x = math.pow(n,2)
    y = math.pow(n,3)

    if x % 2 != 0:
        count += 1

    if y % 3 != 0:
        count_1 += 1

    else:
        pass
        #print(n)
    n = n - 1

print('No of not perfect square in ',i, 'are:',count)
print('No of not perfect square in ',i, 'are:',count_1)