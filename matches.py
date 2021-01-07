# Write a function called matches that takes two strings as arguments and returns how many
# matches there are between the strings. A match is where the two strings have the same char-
# acter at the same index. For instance, ' python ' and ' path ' match in the first, third, and
# fourth characters, so the function should return 3.





def matches(s1 , s2):
    count = 0
    
    # Always take second string as a match and math second with first
    for i in s2:
        if i in s1:
            count += 1
       
    return count






print(matches("Python" , "Path"))