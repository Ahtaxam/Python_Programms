# This programm will calculate the no of second and mn in a seconds

print("Enter the no of sec: ")
sec = int(input())

hrs = sec // 3600
f = hrs * 3600
f = sec - f

minutes = f // 60

seconds = sec % 60

print("Hours in ", sec ," Seconds are: ",hrs)

print("Minutes in ", sec ," Seconds are: ",minutes)

print("Seconds in ", sec ," Seconds are: ",seconds)