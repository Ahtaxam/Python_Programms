
# this programm convert date from mm/dd/yy format into updated format




print('Enter a date in format (mm/dd/yy): ',end='')
s = input()

d= ['01' , '02' ,' 03' , '04' , '05' , '06' , '07' , '08' , '09' , '10' , '11' ,'12']
m = ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'september' , 'october' , 'november' , 'december']
l =[]
for i in s:

    j = 0
    if i == '/':
        continue
    else:
        c = s[j] + s[j+1]
        f = d.index(c)
    j += 1

month = m[f]
year = ''
year += s[-2:]
year = '19' +year

print(month + ' '+s[3:5]+' ' + year)


