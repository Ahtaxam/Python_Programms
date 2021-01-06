# convert temp F to C and vice versa


# celcius to Farenhite
print("Enter the temperature in Celcius: ",end='')
c = int(input())

f = ((9 / 5) * c) + 32
print(c , 'Celcius = ', f , 'farenhite')



#Farenhite to Celcius
print('Enter the temperature in farenhite: ',end='')
f = int(input())

c = (f - 32)
cal = (5 / 9) * c
print(f,"Farenhite = " ,cal , "celcius")


