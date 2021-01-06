# Algo for selection sort



l = [7,4,10,8,3,1,56,0,45,6]

x = len(l)

temp = 0
for i in range(x):

    minimum_element = i
    y = i

    for j in range(i,x):

        if l[j] < l[minimum_element]:
            minimum_element = j

    # swap the element
    temp = l[minimum_element]
    l[minimum_element] = l[i]
    l[i] = temp


print('Sorted list is: ',l)
