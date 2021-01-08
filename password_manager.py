# Write a class called Password_manager . The class should have a list called old_passwords
# that holds all of the user’s past passwords. The last item of the list is the user’s current pass-
# word. There should be a method called get_password that returns the current password
# and a method called set_password that sets the user’s password. The set_password
# method should only change the password if the attempted password is different from all
# the user’s past passwords. Finally, create a method called is_correct that receives a string
# and returns a boolean True or False depending on whether the string is equal to the current
# password or not.




class password_manager:
    old_password = ['abcxy' , 'abcxyz' , '12345abc' , '245abcx']

    
    def get_password(self):
        return self.old_password[-1]
    
    def set_password(self):
        count = 0
        #current_password = self.old_password.pop()
        
        '''First remove the last password bcoz we check the password from past password while last password is 
        current password'''

        
        print('Create Password: ',end='')
        pswd = input()

        '''Through loop check the avaliability of passworrd'''

        for i in range(len(self.old_password) - 1):
            
            if pswd == self.old_password[i]:
                count += 1
            else:
                pass

        if count == 0:
            print('Password Created Successfully')
        else:
            print('Password Already Taken')
        return pswd



    def is_correct(self,string):
        current_password = self.old_password.pop()
        if string == current_password:
            return True
        else:
            return False



password = password_manager()
print(password.get_password())

set_pswd = password.set_password()
print('Password is: ',set_pswd)

print(password.is_correct(set_pswd))



