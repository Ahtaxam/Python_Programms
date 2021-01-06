# gerarate a strong password in python

import random


char = 'abcdefghijklmnopqrstuvwxyz'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'


difficult = char + letter + num 
easy = char + num

#x = random.choice(difficult)
password = ''



# password difficulty level
print('Create Password:  (1) diffiult , (2) Easy:  ',end='')
choice = int(input())



if choice == 1:
    print('Enter the password length: ',end='')
    n = int(input())

    for i in range(n):
        password += random.choice(difficult)
        
        

# check for easy password
elif choice == 2:
    print('Enter the password length: ',end='')
    n = int(input())

    for i in range(n):
        password += random.choice(easy)
else:
    print('Please enter valid Choice')



print()
print('The Password is: ',password)




