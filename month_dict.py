
# This programm tell about no of days in month and many more

days = { 'January' :31, 'February' :28, 'March' :31, 'April' :30,
'May' :31, 'June' :30, 'July' :31, 'August' :31,
'September' :30, 'October' :31, 'November' :30, 'December' :31}


print('Enter the name of month: ',end='')
name = input()
name = name.title()

print('No of days  are: ',days[name])

print()

print("Month which are of 31 days")
for i,j in days.items():
    if j == 31:
        print(i , end=' , ')
print()



print()
# sort dictionaty by values

l = []
for i in sorted(days.items() , key = lambda x : x[1]):
    l.append(i)
    
l = dict(l)
print("Dictionary sorted by no of days")
print(l)