# Write a program to play the following simple game. The player starts with $100. On each
# turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
# correct guess and loses $10 for each incorrect guess. The game ends either when the player
# runs out of money or gets to $200.



import random

money = 100





while money >= 0 and money <= 200:

    rd = random.randint(1,2)

    print('Flip a coin (1 --> Head , 2 --> Tail): ',end='')
    coin = int(input())

    if coin == rd:
        money += 9

    else:
        money -= 10



if money > 0:
    print('You Win: ',money)
else:
    print('You loose',money)

