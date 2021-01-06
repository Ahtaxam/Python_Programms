print('Checking Student and professor Email ')

print("How many email you want to entered: ",end='')
n = int(input())

l = []
Student_mail = 0
professor_mail = 0

while n > 0:
    print('Enter an Email address: ',end=' ')
    email = input()

    l.append(email)

    n -= 1

for check in l:
    if check[-1] == ',':
        Student_mail += 1
    else:
        professor_mail += 1


print('Student email are: ',Student_mail)
print('Profrssor email are: ',professor_mail)