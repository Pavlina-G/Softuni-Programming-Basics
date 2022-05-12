hour = int(input())
week_day = input()

if week_day != 'Sunday' and 10 <= hour <= 18:
    print('open')
else:
    print('closed')
