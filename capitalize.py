# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So if the user enters rhinoceros , the program should print rHiNoCeRoS .




print("Enter a string: ",end='')
s = input()

w = ''
se = ''
for letter in s:
    
    i = s.index(letter)
    if i % 2 != 0:
        letter = letter.capitalize()
        w += letter
    else:
        w += letter

print(w)
#print(se)