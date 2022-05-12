num = int(input())
if num < 100:
    print('Less than 100')
elif 100 <= num <= 200:
    print('Between 100 and 200')
elif num > 200:
    print('Greater than 200')

# Second way
num = int(input())
if num < 100:
    print('Less than 100')
elif num <= 200:
    print('Between 100 and 200')
elif num > 200:
    print('Greater than 200')

# 3 way
num = int(input())
if num < 100:
    print('Less than 100')
elif 100 <= num <= 200:
    print('Between 100 and 200')
else:
    print('Greater than 200')