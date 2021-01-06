
import math

print('Enter the value of n: ',end='')
n = int(input())

sm = 0

for i in range(2,n+1):
    sm +=  (1/i)
    s = sm + 1

    # calculate log
    log = math.log(n)
    
    # minus the log in series
    series = s - log

print('Sum of series is: ',series)
