holidays = int(input())
yearly_game_min = 30000
daily_work_game_min = 63
day_off_game_min = 127
year = 365

days_off_time = holidays * day_off_game_min
work_day_time = (year - holidays) * daily_work_game_min
total_time = days_off_time + work_day_time
difference = abs(total_time - yearly_game_min)
hours = difference // 60
minutes = difference % 60

if total_time > yearly_game_min:
    print(f"Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')


