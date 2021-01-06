import random as rd

right = 0
wrong = 0

print("--------------------Question 1" )
print("Qusetion 1: 3 x 4 = ",end='')
no_1 = rd.randint(1,20)
print(no_1)
if no_1 == 3*4:
    print("Right")
    right += 1
else:
    print("wrong")
    wrong += 1



print("--------------------Question 2" )

print("Qusetion 1: 7 x 4 = ",end='')
no_1 = rd.randint(1,100)
print(no_1)
if no_1 == 7*4:
    print("Right")
    right += 1
else:
    print("wrong")
    wrong += 1




print("--------------------Question 3" )

print("Qusetion 1: 5 x 4 = ",end='')
no_1 = rd.randint(1,100)
print(no_1)
if no_1 == 5*4:
    print("Right")
    right += 1
else:
    print("wrong")
    wrong += 1





print("--------------------Question 4" )

print("Qusetion 1: 10 x 4 = ",end='')
no_1 = rd.randint(1,100)
print(no_1)
if no_1 == 10*4:
    print("Right")
    right += 1
else:
    print("wrong")
    wrong += 1



print("--------------------Question 5" )

print("Qusetion 1: 9 x 9 = ",end='')
no_1 = rd.randint(1,100)
print(no_1)
if no_1 == 9*9:
    print("Right")
    right += 1
else:
    print("wrong")
    wrong += 1



print("Wrong Answer are: ",wrong)
print("Right Answer are: ",right)