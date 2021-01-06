
# this programm demonstrate the perfect no

print('Enter a no: ',end='')
n = int(input())

i = n-1
sm = 0

while i > 0:
    if n % i == 0:
        sm += i
    
    else:
        pass
    i -= 1


# if sum of input no is equal to the input then it is perfect no

if n == sm:
    print(n,"is a Perfect Square")
else:
    print(n,'is Not a Perfect square')