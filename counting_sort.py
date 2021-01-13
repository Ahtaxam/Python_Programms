# This Programm demonstrate counting sort

def counting(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0 , size):
        count[array[i]] += 1

    for i in range(1 , size):
        count[i] = count[i] + count[i - 1]


    i = size - 1

    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1


    for i in range(0 , size):
        array[i] = output[i]




data = [4,3,5,3,1,7,1,0]

print('Original Array is: ', data)
print()
counting(data)

print('Sorted Array is: ',data)