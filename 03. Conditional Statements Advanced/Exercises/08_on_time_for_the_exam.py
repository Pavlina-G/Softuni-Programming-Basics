hour_of_exam = int(input())
minutes_of_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
# Convert the time in minutes
time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arrival = arrival_hour * 60 + arrival_minutes

if time_of_arrival > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On time")
else:
    print("Early")
# or time_of_exam- 30 > time_of_arrival

difference = abs(time_of_arrival -  time_of_exam)
hours = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{difference} minutes before the start')
elif time_of_arrival <= time_of_exam- 60:
    if minutes < 10:
        print(f'{hours}:0{minutes} hours before the start')
    else:
        print(f'{hours}:{minutes} hours before the start')
#     {minutes:02d} same as 0{minutes}
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{difference} minutes after the start')
elif time_of_arrival >= time_of_exam + 60:
    if minutes < 10:
        print(f'{hours}:0{minutes} hours after the start')
    else:
        print(f'{hours}:{minutes} hours after the start')