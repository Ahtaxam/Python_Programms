# Write a program that asks the user to enter a string, then prints out each letter of the string
# doubled and on a separate line. For instance, if the user entered HEY , the output would be

# HH
# EE
# YY


print('Enter a string: ',end=' ')
s = input()

for i in s:
    print(i*2)
    