from math import ceil

tv_series = (input())
series_duration = int(input())
break_duration = int(input())

time_for_lunch = 1/8 * break_duration
time_to_relax = 1/4 * break_duration
left_time = break_duration - time_to_relax - time_for_lunch
difference_time = abs (series_duration - left_time)

if left_time >= series_duration:
    print(f"You have enough time to watch {tv_series} and left with {ceil(difference_time)} minutes free time.")
else:

    print(f"You don't have enough time to watch {tv_series}, you need {ceil(difference_time)} more minutes.")