
# The number 99 has the property that if we multiply its digits together and then add the sum
# of its digits to that, we get back to 99. That is, (9 × 9) + (9 + 9) = 99 . Write a program to find
# all of the numbers less than 10000 with this property. (There are only nine of them.)



i = 0
sm = 0
sm1 = 0
pro = 0
count = 0
while i < 10000:
    # first convert it into string
    i = str(i)

    # first find that no consist of 2 dogit
    if len(i) >= 2:
        sm = i[0]
        sm1 = i[1]

        #convert string into int
        sm = int(sm)
        sm1 = int(sm1)

       # compute using formula
        x = (sm * sm1) + (sm + sm1)
        i = int(i)

        #check condition
        if x == i:
            count += 1


    i = int(i)
    i += 1 

print('Total no are: ',count)


