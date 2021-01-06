# Write a program that asks the user to enter a word. Rearrange all the letters of the word
# in alphabetical order and print out the resulting word. For example, abracadabra should
# become aaaaabbcdrr .


print('Enter a word: ',end='')
word = input()

x = ''
for letter in  word:
    count  = word.count(letter)
    s = letter * count
    if s not in x:
        x += s


y = sorted(x)
y = ''.join(y)

print('Arranging Word is: ',y)

