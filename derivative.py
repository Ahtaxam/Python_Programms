print('Enter a expression: ',end='')
x = input()

# x^5
y = x[-1] # y = 5

z = int(y)  # z = int ---> 5

ans = z - 1 # ans = 4

z = str(z)  # z = str------> 5
ans = str(ans) # ans = str------> 4
y = z + x[0] 
y += ans

print("The derivative of Expression is: ",y)


