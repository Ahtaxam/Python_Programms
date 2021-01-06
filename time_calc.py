# this programm ask hours and convert them into time according to AM and PM


print("Enter an hous 1 to 12: ",end='')
hrs_1 = int(input())

print("Enter time format (am - 1  , pm - 2): ",end='')
sign = int(input())

print('How many hours you want to go: ',end='')
hrs_2 = int(input())


s = hrs_1 + hrs_2
if s > 12 and sign == 1:
    r = s % 12
    print(r,'PM')

elif s > 12 and sign == 2:
    r = s % 12
    print(r,"AM")

elif s < 12 and sign == 1:
    print(s,'AM')

else:
    print(s,'PM')



