# Write a function called closest that takes a list of numbers L and a number n and returns
# the largest element in L that is not larger than n . For instance, if L=[1,6,3,9,11] and n=8 ,
# then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than
# 8. Don’t worry about if all of the things in L are smaller than n .




def closest(l,n):
    l1 = []
    for i in l:
        # first we using condition find the lowest all no than n and append into list
        if i < n:
            l1.append(i)

    # than in the update list we find the maximum no that will be our target
    x = max(l1)
    return x







l = [1,7,13,9,11]
n = 18
print(closest(l,n))