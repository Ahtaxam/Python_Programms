
# This programm will encrypt the stirng into even odd

print('Enter a String:  ',end=' ')
m = input()


e = ''
d = ''


for i in range(len(m)):
    if i % 2 == 0:
        e += m[i]
    else:
        d += m[i]


encrypt = e + d
print("....................")
print('Encrypted String is: ',encrypt)


#               Decrypt the same Message


x = 0
Decrypt = ''



for j in m:
    x = encrypt.find(j)
    Decrypt += encrypt[x]
print("....................")
print("The Decrypted of encrypted is: ",Decrypt)