# Write a program that uses a dictionary that contains ten user names and passwords. The
# program should ask the user to enter their username and password. If the username is not in
# the dictionary, the program should indicate that the person is not a valid user of the system. If
# the username is in the dictionary, but the user does not enter the right password, the program
# should say that the password is invalid. If the password is correct, then the program should
# tell the user that they are now logged in to the system.





user_dict = {
    'Admin' : 'abcd1234' , 
    'computer' : 'password' ,
    'ali'  : '12345678' ,
    'alpha' : 'abcxyz' 
}


print('Enter the User_name: ',end='')
name = input()

if name not in user_dict.keys():
    print('Person is not  valid')

else:
    print('Enter the password: ',end='')
    pswd = input()

    if pswd not in user_dict.values():
        print('Password Incorrect')
    
    else:
        print('You are now loged into system')


