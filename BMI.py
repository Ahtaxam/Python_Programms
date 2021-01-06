# Body mass index calculator


print("Enter the Unit for mass  (k/K for kilogram , p/P for pound): ",end='')
unit_m = input()
unit_m =  unit_m.lower()

if unit_m == 'k':

    print("Enter your weight in kilogram: ",end='')
    weight = int(input())

    print('Enter the unit for height(M/m for meters, I/i for inches): ',end='')
    unit_h = input()

    #condition for check unit of height
    if unit_h == 'i':
        print("Enter your height in inches: ",end='')
        height = int(input())
        height = height / 39.37

    else:
        print('Enter the height in meter: ',end='')
        height = int(input())
    

#   if height in pound then below code will run


else:

    print("Enter your weight in pound: ",end='')
    weight = int(input())
    weight = weight * 2.205

    #condition for check unit of height
    print('Enter the unit for height(M/m for meters, I/i for inches): ',end='')
    unit_h = input()
    unit_h = unit_h.lower()

    if unit_h == 'i':
        print("Enter your height in inches: ",end='')
        height = int(input())
        height = height / 39.37

    else:
        print('Enter the height in meter: ',end='')
        height = int(input())



# calculate BMI
BMI = (weight) / (height * height)
print(BMI)

# condition code 

if BMI <= 18.5:
    print("UnderWeight")

elif BMI > 18.5 and BMI < 25:
    print("healthy")

elif BMI >= 25 and BMI < 30:
    print("Overweight")

else:
    print("Obese")