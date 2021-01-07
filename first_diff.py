
# This function will return the index of element where element of list are different


def first_diff(s1,s2):
    i = 0
    for i in range(len(s1)):

        # Do nothing
        if s1[i] == s2[i]:
           pass

        # return address
        else:
            x = i
            return x



z = first_diff('ahtasham' , 'ahtimama')
print('Index: ',z)