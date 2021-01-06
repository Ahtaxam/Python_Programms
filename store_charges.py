#this program calculate cost

print("Enter the items that you buy: ",end='')
item = int(input())

cost = 0

if item < 10:
    charges = item * 12
    cost = item + charges

elif item >= 10 and item <= 99:
    charges = item * 10
    cost = item + charges

else:
    charges = item * 7
    cost = item + charges


print('Total cost is: ',cost)
