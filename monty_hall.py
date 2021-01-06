# this programm is about a little playing game

hidden_1 = 'Oh ! Congrats You win a prize'
hidden_2 = "Goats"
hidden_3 = "Goats"

average = 0
Switching = 0

playing = 5

while playing > 0:

    print('Hey ! Pick up a door: ',end='')
    n = int(input())

    if n == 1:
        print(hidden_1)
        average += 1

    else:
        print('!!!!  Warning')
        print('Hey ! You choose a wrong door do you want to switch the door: ',end='')
        choose = input()

        if choose == 'yes':
            Switching += 1
            print('Wait ! Switching')
                
        else:
            print(hidden_2)
    playing -= 1
            

    

    

print('without Switching : ',average)
print('Switching : ',Switching)



