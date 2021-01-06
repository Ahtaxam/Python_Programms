# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product
# name and print the corresponding price or a message if the product is not in the dictionary.




d = {}

item = 5
while item > 0:

    print('Enter a Product Name: ',end='')
    name = input()

    print('Enter the Price of Product: ',end='')
    price = int(input())

    print()
    d[name] = price
    item -= 1


print("Pleaes Enter the Name of product: ",end='')
prod = input()

if prod not in d:
    print("product is not in dictionary")
else:
    print(d[prod])

print()

print('Enter a dollar amount: ',end='')
dollar = int(input())



print('These values are less than given amount')
for values in d.values():
    if values < dollar:
        print(values, end='')
    print()


