#this programm is a kid game that is rock paper scissors

import random 


man = 0
comp = 0

i = 5
while i > 0:
    computer_no = random.randint(1,100)

    print('Enter a guess number: ',end='')
    no = int(input())

    print('Computer generate: ',computer_no)

    if no != computer_no:
        man += 1

    else:
        comp += 1

    i -= 1


if man > comp:
    print('You Win')

elif man < comp:
    print('Computer Win')

else:
    print('Game Tie')


