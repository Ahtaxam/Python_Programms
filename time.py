class Time:

    def convert_to_minute(self,seconds):
        minutes = seconds // 60
        second  = seconds % 60
        return "'{}:{}'".format(minutes , second)

    def convert_to_hour(self,Seconds):
        hrs = Seconds // 3600
        f = hrs * 3600
        f = Seconds - f
        minutes = f // 60
        Second = Seconds % 60
        return "'{}:{}:{}'".format(hrs,minutes,Second)





time = Time()

print('Enter no of Seconds: ',end='')
sec = int(input())
print(time.convert_to_minute(sec))


print('Enter the no of Seconds: ',end='')
sec = int(input())
print(time.convert_to_hour(sec))