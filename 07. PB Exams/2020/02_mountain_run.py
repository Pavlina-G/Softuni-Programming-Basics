from math import floor

record_seconds = float(input())
distance_m = float(input())
time_sec_per_meter = float(input())

time = time_sec_per_meter * distance_m
additional_time = floor(distance_m / 50) * 30
time = additional_time + time
difference = abs(record_seconds - time)

if time < record_seconds:
    print(f"Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")

