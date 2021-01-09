# This programm demonstrate a little game 

import random

rd = random.randint(1,10)

chances = 7

status = ''
try_ = 1

print('<-----Number Guessing Game------>')
while chances > 0:

    print('Enter a no Between 1 to 10 to Guess: ',end='    ')
    no = int(input())

    if no == rd:
        print('You won the game in {} tries'.format(try_))
        break

    elif no > rd:
        print('you guess too high number')

    elif no < rd:
        print('you guess too low number')
    print()
    try_ += 1
    chances -= 1

if no != rd:
    print('You Loose')




