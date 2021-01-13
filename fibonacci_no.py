# find the fibinacci no

# This algo very slow and can break the programmm 

def fabrecu(n):
    if n <= 1:
        return n
    else:
        return fabrecu(n - 2) + fabrecu(n - 1)


print('Enter the no: ',end='')
no = int(input())

print(fabrecu(no))




# This algo is very very fast


print('Enter the no: ',end='')
n = int(input())

lst = [None] * n
lst[0] = 0
lst[1] = 1

for i in range(2 , n):
    lst[i] = lst[ i - 2 ] + lst[i - 1]


print(lst)