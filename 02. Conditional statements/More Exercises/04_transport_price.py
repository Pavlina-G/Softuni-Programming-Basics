distance_km = int(input())
day_or_night = input()
price = 0
taxi_rate = 0

if day_or_night == 'day':
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if distance_km < 20:
    price = 0.70 + (distance_km * taxi_rate)
elif distance_km < 100:
    price = distance_km * 0.09
else:
    price = distance_km * 0.06
print(f'{price:.2f}')


