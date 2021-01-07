# Write a function that takes an integer n and returns a random integer with exactly n digits. For
# instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
# that is really 93, which is a two-digit number.



import random

def integer(n):

    rd = random.randint(1,1000)

    # first convert into string
    s = str(rd)

    # then find length of random no
    l = len(s)

    # Now check condition given
    if l == n and s[0] != '0':
        return rd

    # In case of false condition
    else:
        print('Else case')
        return rd








print(integer(3))