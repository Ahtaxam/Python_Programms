# Write a program that asks the user to guess a random number between 1 and 10. If they guess
# right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
# the user five numbers to guess and print their score after all the guessing is done.


import random as rd

chances = 5
score = 0

while chances > 0:

    guess = rd.randint(1,10)

    print('Enter a guess no: ',end='')
    n = int(input())

    print("Computer generate: ",guess)

    if n == guess:
        score += 10
    else:
        score -= 1
    chances -= 1


print("Overall score is: ",score)


