# Recall that if s is a string, then s.find( ' a ' ) will find the location of the first a in s . The
# problem is that it does not find the location of every a. Write a function called findall that
# given a string and a single character, returns a list containing all of the locations of that char-
# acter in the string. It should return an empty list if there are no occurrences of the character
# in the string.


def find_all(s,find):
    loc = 0
    l = []

    # using loop compare the letter where match
    for i in s:
        if i == find:

            # Now find the index of letter
            x = s.find(find , loc)

            # Append into list
            l.append(x)
        loc += 1
    return l

   
present = find_all('ahtashama' , 'a')

print("The letter present at at locations: ",present,end=' ')
print()