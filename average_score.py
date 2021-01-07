# This  programm calculate the winning and lossing percentage of a team 


info = {}

repeat = 3
l1 = []
l2 = []
l3 = []

while repeat > 0:
    if repeat == 3:
        print('Enter the team name: ',end='')
        name = input()

        print("Enter the game they wone : ",end='')
        win = int(input())
        print("Enter the game they lose : ",end='')
        lose = int(input())
        l1.append(win)
        l1.append(lose)

        info[name] = l1

    elif repeat == 2:
        print('Enter the team name: ',end='')
        name = input()

        print("Enter the game they wone : ",end='')
        win = int(input())
        print("Enter the game they lose : ",end='')
        lose = int(input())
        l2.append(win)
        l2.append(lose)

        info[name] = l2


    elif repeat == 1:
        print('Enter the team name: ',end='')
        name = input()

        print("Enter the game they wone : ",end='')
        win = int(input())
        print("Enter the game they lose : ",end='')
        lose = int(input())
        l3.append(win)
        l3.append(lose)

        info[name] = l3

    repeat -= 1

print('Enter the team name: ',end='')
team = input()
winning_match = info[team][0]
print('The winning match of team is: ',winning_match)


print(info)