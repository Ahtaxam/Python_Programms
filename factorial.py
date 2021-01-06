# this programm print factorial of that number

print("Enter a number: ")
no = int(input())

i = no
fact = 1

while i != 0:
    fact *= i
    i -= 1

print("factorial of " , no , " is: ",fact)
    