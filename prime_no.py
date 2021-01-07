#check weather a number is prime or not



print("Enter Number to find prime: ",end='')
no = int(input())


for i in range(2,no-1):
    if no % i == 0:
        print("{} is not prime number".format(no))
        break


if i == no - 1:
    print("Number is Prime")




#               <---------------------------------------------->






#                        Another Approach


status = ''

for i in range(2,no-1):
    x = no % i
    if x == 0:
        status = '{} is not Prime no'.format(no)
        break
    else:
        status = "{} is  prime number".format(no)


print(status)


