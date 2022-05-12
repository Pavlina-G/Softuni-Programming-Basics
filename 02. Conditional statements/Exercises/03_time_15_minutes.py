hour = int(input())
minutes = int(input())

# all time in minutes + 15 min after
total_time = hour * 60 + minutes + 15

# time in hours - whole number
total_time_h = total_time // 60

# time in minutes = the remaining time with %
total_time_m = total_time % 60

# time 0-23
if total_time_h == 24:
    total_time_h = 0

if total_time_m < 10:
    print(f'{total_time_h}:0{total_time_m}')
else:
    print(f'{total_time_h}:{total_time_m}')

# Second way

hour = int(input())
minutes = int(input())
minutes += 15

# new minutes to hours
hour += minutes // 60

# the rest of the minutes
minutes %= 60

if hour > 23:
    hour = 0
if minutes <= 9:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')






