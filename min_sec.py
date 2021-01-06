# This programm will calculate the no of second and mn in a seconds

print("Enter the no of sec: ")
sec = int(input())

hrs = sec // 3600

minutes = hrs // 60

seconds = sec % 60

print("Hours in ", sec ," Seconds are: ",hrs)

print("Minutes in ", sec ," Seconds are: ",minutes)

print("Seconds in ", sec ," Seconds are: ",seconds)