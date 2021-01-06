#This program check the weather a entered  password is valid or not


pwsd = 'abc12345'

chances = 5

while chances > 0:
    print('Enter Password: ',end=' ')
    p = input()

    if p == pwsd:
        print('Loged ! Into System')
        break
    else:
        print('Warning !!!!!!!')
        print('Reenter the Password: ',end=' ')
        p = input()
        if p == pwsd:
            print("Loged Successfully ! ")
            break
        else:
            print('Again wrong')
    
    chances -= 1

