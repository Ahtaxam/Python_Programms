# Bubble sort algorithm
import time
start_time = time.time()


    # Sorting with function

def swap(l,x,i):
    temp = l[x]
    l[x] = l[i]
    l[i] = temp


temp = 0
l = [3,45,1,56,78,9,0]

x = len(l)

for i in range(x):
    for j in range(x):

        # if condition true then call function
        if l[j] > l[i]:
            swap(l,j,i)
print(l)

print('Time is: ' , time.time() - start_time)




print("> ----------------------------------------------- <")





#                   Sorting without function







temp = 0
l = [3,45,1,56,78,9,0]

x = len(l)

for i in range(x):
    for j in range(x):

        # if condition true then swap
        if l[j] > l[i]:

            temp = l[j]
            l[j] = l[i]
            l[i] = temp
            
print(l)

print('Time is: ' , time.time() - start_time)




print("> ----------------------------------------------- <")