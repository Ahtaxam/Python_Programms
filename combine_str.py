

print("Enter a string of lower case letter: ",end='')
a = input()

print('Enter a string of Capital case letter: ',end='')
A = input()

l = ''

for i in range(len(a)):
    s = A[i] + a[i]
    l += s

print('combine string is: ',l)


