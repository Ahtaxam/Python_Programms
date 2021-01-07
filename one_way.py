# Write a function called one_away that takes two strings and returns True if the strings are of
# the same length and differ in exactly one letter, like bike/hike or water/wafer .



def one_way(s1,s2):
    count = 0

    # first compare that length are same
    if len(s1) == len(s2):

        # through loop find the behaviour that they satisfied condition
        for i in s1:
            if i in s2:
                count += 1
            else:
                pass
        if count == len(s1) - 1:
            return True
        else:
            return False

# some input to check the code
x = one_way('bike' , 'hike') # True
y = one_way('water' , 'wafer') # True
z = one_way('abcd' , 'abxy')  # False

print(x)
print(y)
print(z)