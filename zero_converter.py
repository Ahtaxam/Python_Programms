
import random as rd


lst = [1,1,1,1,0,1,1]
x = ' '

for i in range(len(lst)):

    if lst[i] == 0:
        lst[i] = 1
        break

    else:
        if 0 not in lst:
            x = 'No Zero present'
            




print(x)
print(lst)
