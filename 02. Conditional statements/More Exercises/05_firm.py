from math import floor

hours = int(input())
days = int(input())
employees_overtime = int(input())

time = 0
time = floor(days * 8 * 0.9)
overtime = days * 2 * employees_overtime
time = time + overtime
difference = abs(time - hours)

if time >= hours:
    print(f'Yes!{floor(difference)} hours left.')
else:
    print(f'Not enough time!{floor(difference)} hours needed.')