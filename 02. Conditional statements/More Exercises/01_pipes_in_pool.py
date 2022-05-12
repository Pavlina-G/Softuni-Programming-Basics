volume_l = int(input())
pipe1_per_hour = int(input())
pipe2_per_hour = int(input())
absent_hours = float(input())

water1 = pipe1_per_hour * absent_hours
water2 = pipe2_per_hour * absent_hours
water = water1 + water2

volume = water / volume_l * 100
volume1 = (water1) / water * 100
volume2 = (water2) / water * 100

if water > volume_l:
    difference = water - volume_l
    print(f"For {absent_hours} hours the pool overflows with {difference:.2f} liters.")
else:
    print(f"The pool is {volume:.2f}% full. Pipe 1: {volume1:.2f}%. Pipe 2: {volume2:.2f}%.")
